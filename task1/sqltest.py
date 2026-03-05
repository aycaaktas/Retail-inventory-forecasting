import sqlite3
import pandas as pd

# File paths for the CSV files
inventory_file = "inventory_position_table.csv"
store_file = "store_table.csv"

# Creating an in-memory SQLite database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Creating tables
cursor.execute("""
CREATE TABLE InventoryPositionTable (
    Date DATE,
    StoreCode INT,
    ProductCode TEXT,
    SalesQuantity INT,
    SalesRevenue FLOAT,
    ShipmentQuantity INT,
    StoreStock INT,
    IncomingStock INT
);
""")
cursor.execute("""
CREATE TABLE StoreTable (
    StoreCode INT,
    StoreDescription TEXT,
    IsBlocked BOOLEAN,
    StoreDetailedCode INT,
    SalesChannelType TEXT,
    Location INT,
    BuildingType TEXT
);
""")

# Loading data from CSV files into pandas DataFrames
inventory_df = pd.read_csv(inventory_file)
store_df = pd.read_csv(store_file)

# Inserting data into tables from DataFrames
inventory_df.to_sql("InventoryPositionTable", conn, if_exists="replace", index=False)
store_df.to_sql("StoreTable", conn, if_exists="replace", index=False)

# Queries
queries = {
    "Latest StoreStock": """
        WITH LatestDates AS (
            SELECT StoreCode, ProductCode, MAX(Date) AS LatestDate
            FROM InventoryPositionTable
            GROUP BY StoreCode, ProductCode
        )
        SELECT t.StoreCode, t.ProductCode, t.StoreStock, d.LatestDate
        FROM InventoryPositionTable t
        JOIN LatestDates d
        ON t.StoreCode = d.StoreCode AND t.ProductCode = d.ProductCode AND t.Date = d.LatestDate;
    """,
    "Sum Sales by BuildingType": """
        SELECT s.BuildingType, SUM(ip.SalesRevenue) AS TotalRevenue
        FROM InventoryPositionTable ip
        JOIN StoreTable s ON ip.StoreCode = s.StoreCode
        GROUP BY s.BuildingType;
    """,
    "Stores with Revenue lower than 50 in May 2014": """
        SELECT s.StoreCode, s.StoreDescription
        FROM InventoryPositionTable ip
        JOIN StoreTable s ON ip.StoreCode = s.StoreCode
        WHERE ip.Date BETWEEN '2014-05-01' AND '2014-05-31'
        GROUP BY s.StoreCode, s.StoreDescription
        HAVING SUM(ip.SalesRevenue) < 50;
    """,
    "Revenue Difference in Feb 2014": """
        WITH FebruarySales AS (
            SELECT ip.StoreCode, SUM(ip.SalesRevenue) AS TotalRevenue
            FROM InventoryPositionTable ip
            WHERE ip.Date BETWEEN '2014-02-01' AND '2014-02-28'
            GROUP BY ip.StoreCode
        ),
        MaxMinRevenue AS (
            SELECT
                MAX(TotalRevenue) AS MaxRevenue,
                MIN(TotalRevenue) AS MinRevenue
            FROM FebruarySales
        )
        SELECT 
            MaxRevenue - MinRevenue AS RevenueDifference,
            (SELECT StoreCode FROM FebruarySales WHERE TotalRevenue = (SELECT MaxRevenue FROM MaxMinRevenue)) AS MaxRevenueStoreCode,
            (SELECT StoreCode FROM FebruarySales WHERE TotalRevenue = (SELECT MinRevenue FROM MaxMinRevenue)) AS MinRevenueStoreCode
        FROM MaxMinRevenue;

    """
}

# Executing each query and saving the results to separate files
for query_name, query in queries.items():
    result = pd.read_sql_query(query, conn)
    output_file = f"{query_name.replace(' ', '_').lower()}.csv"
    result.to_csv(output_file, index=False)
    print(f"Query '{query_name}' results saved to {output_file}")

# Closing the database connection
conn.close()
