# 📊 Retail Data Analytics Case Study

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange?logo=sqlite)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?logo=tableau)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

SQL | Data Analysis | Forecasting | Dashboard | Business Intelligence

This project is a **data analytics case study on retail inventory and sales data**.  
It includes **SQL-based data transformations, sales analysis, inventory insights, and forecasting analysis** using Python and visualization tools.

The goal of the project is to **analyze retail performance, understand inventory behavior, and derive insights from actual and forecasted sales data**.

---

# 🧠 Project Overview

The project consists of **two main tasks**:

### Task 1 — SQL Data Analysis
Focuses on **inventory and sales data transformations using SQL queries**.

Key objectives:
- Identify the **latest store stock levels**
- Calculate **sales revenue by building type**
- Detect **stores with low revenue**
- Compare **sales performance across stores**

### Task 2 — Forecasting & Inventory Analysis
Focuses on **data cleaning, preparation, and analytics on forecasted sales data**.

Key objectives:
- Clean and prepare datasets
- Merge product and forecasting data
- Analyze **inventory, stockouts, revenue, and profitability**
- Identify **patterns between historical and forecasted data**

The project demonstrates **end-to-end analytics workflow including SQL, Python data processing, and dashboard visualization**.

---

# 📂 Project Structure

```
retail-data-analytics-case-study
│
├── task1
│   ├── inventory_position_table.csv
│   ├── store_table.csv
│   ├── sqltest.py
│   ├── latest_storestock.csv
│   ├── sum_sales_by_buildingtype.csv
│   ├── stores_with_revenue_lower_than_50_in_may_2014.csv
│   └── revenue_difference_in_feb_2014.csv
│
├── task2
│   ├── future_visibility.csv
│   ├── products.csv
│   ├── prep_analysis.ipynb
│   ├── final_analysis_actual_data.csv
│   ├── final_analysis_forecasted_data.csv
│   └── final_analysis_merged_data.csv
│
├── analysis.twbx
├── analysis.pptx
└── Data Analyst Case.pptx
```

---

# 🧩 Task 1 — SQL Data Analysis

Task 1 analyzes **inventory and store sales data using SQL queries**.

The Python script loads CSV data into an **in-memory SQLite database** and executes SQL queries automatically.

Main script:

```
task1/sqltest.py
```

The script:

1. Creates SQLite tables
2. Loads CSV datasets
3. Executes analytical SQL queries
4. Saves results as CSV outputs

Example queries include:

### Latest StoreStock per Store and Product
```sql
WITH LatestDates AS (
SELECT StoreCode, ProductCode, MAX(Date) AS LatestDate
FROM InventoryPositionTable
GROUP BY StoreCode, ProductCode
)
SELECT t.StoreCode, t.ProductCode, t.StoreStock
FROM InventoryPositionTable t
JOIN LatestDates d
ON t.StoreCode = d.StoreCode 
AND t.ProductCode = d.ProductCode 
AND t.Date = d.LatestDate;
```

### Sum Sales by Building Type

```sql
SELECT s.BuildingType, SUM(ip.SalesRevenue) AS TotalRevenue
FROM InventoryPositionTable ip
JOIN StoreTable s ON ip.StoreCode = s.StoreCode
GROUP BY s.BuildingType;
```

### Stores with Revenue < 50 TL in May 2014

```sql
SELECT s.StoreCode, s.StoreDescription
FROM InventoryPositionTable ip
JOIN StoreTable s ON ip.StoreCode = s.StoreCode
WHERE ip.Date BETWEEN '2014-05-01' AND '2014-05-31'
GROUP BY s.StoreCode, s.StoreDescription
HAVING SUM(ip.SalesRevenue) < 50;
```

### Revenue Difference Between Highest and Lowest Selling Stores (Feb 2014)

Calculates the difference between **top and bottom performing stores**.

The results of these queries are exported into:

```
latest_storestock.csv
sum_sales_by_buildingtype.csv
stores_with_revenue_lower_than_50_in_may_2014.csv
revenue_difference_in_feb_2014.csv
```

The SQL logic is implemented in the Python script. :contentReference[oaicite:0]{index=0}

---

# 📈 Task 2 — Forecasting & Inventory Analytics

Task 2 focuses on **data cleaning, preparation, and exploratory analysis**.

Datasets used:

- `future_visibility.csv`
- `products.csv`

These datasets were merged and analyzed using Python.

Notebook:

```
task2/prep_analysis.ipynb
```

---

# 🧹 Data Cleaning Steps

- Removed duplicate records
- Handled missing values
- Applied interpolation and median filling where appropriate
- Preserved logical null values for forecast-specific fields

Example:

- Forecast rows contain **Unit_Forecast values**
- Actual rows contain **Unit_TY values**

---

# 📊 Key Analysis Areas

The analysis focused on several key retail performance metrics:

### 1️⃣ Sales & Revenue Analysis

Strong positive correlations were observed between:

- Unit_TY and SalesRevenue_TY
- Unit_LY and SalesRevenue_LY

This confirms that **units sold strongly drive revenue performance**.

---

### 2️⃣ Stockout Analysis

Key observations:

- Higher stockouts correlate with **lower inventory levels**
- Forecasts predict **increased stockout risk for mid-speed products**
- Fast-moving products show **better inventory management**

---

### 3️⃣ Inventory Management

Certain categories showed **inventory buildup**, including:

- Apparel
- Mens Outdoor Tops
- Mens Sports Tops

This may indicate **overstocking or demand overestimation**.

---

### 4️⃣ Profitability Insights

Top performing categories:

- Apparel
- Mens Outdoor Tops
- SS Tops

Underperforming categories:

- Footwear
- Work/Casual Hosiery
- Active FW

These insights highlight **opportunities for strategic adjustments**.

---

# 📊 Dashboard

A dashboard was created to visualize insights including:

- Revenue trends
- Stockout analysis
- Product hierarchy performance
- Forecasted vs actual data comparisons

Dashboard file:

```
analysis.twbx
```

---

# 🛠 Technologies Used

- **Python**
- **SQLite**
- **Pandas**
- **SQL**
- **Jupyter Notebook**
- **Tableau**
- **Data Visualization**

---

# 🚀 How to Run Task 1

Install dependencies:

```bash
pip install pandas
```

Run the SQL analysis script:

```bash
python sqltest.py
```

This will generate query results as CSV files.

---

# 📌 Key Insights

- Apparel categories drive the majority of revenue.
- Footwear categories consistently underperform.
- Inventory buildup indicates possible **forecast inaccuracies**.
- Stockouts strongly correlate with lost sales.
- Forecast models predict **higher variability in demand**.

---


# ⭐ If you found this project interesting

Give it a ⭐ on GitHub!