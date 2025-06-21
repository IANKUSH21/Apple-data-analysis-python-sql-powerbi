# APPLE INC. BUSINESS ANALYTICS PROJECT

![iPhone Banner](https://www.apple.com/v/iphone/home/bv/images/meta/iphone__ky2k6x5u6vue_og.png)

---

## 🔍 OBJECTIVE

Analyze iPhone sales and Apple’s financial performance using Python for data cleaning and exploration, SQL for querying, and Power BI for interactive business dashboards.

---

## 📦 DATA SOURCES

1. **Net\_Sales\_By\_Product\_And\_Service.csv** - iPhone and other product category sales (2022–2024)
2. **Gross\_Margin\_Values.csv** - Gross margins across product types
3. **Segment\_Operating\_Performance.csv** - Regional net sales of Apple

---

## ⚙️ TOOLS & TECHNOLOGIES

* Python (Pandas, Matplotlib, Seaborn, Plotly)
* SQL (MySQL)
* Power BI

---

## 📊 PROJECT INSIGHTS

### 🧪 PYTHON ANALYSIS HIGHLIGHTS

* Cleaned and explored multi-year product sales data
* Calculated Year-over-Year (YoY) growth percentages
* Visualized gross margin trends, category-wise average sales
* Conducted correlation analysis and built a linear regression model to predict 2024 sales
* Generated pie, bar, and line charts to reveal category and regional trends

### 🧠 KEY FINDINGS

* **iPhone** consistently leads in sales across all years
* **Americas** region is the top-performing market in 2024
* **Services** segment shows continuous growth in net sales and margins
* High correlation across 2022–2024 net sales trends
* Products like Mac and iPad saw volatility in YoY performance

---

## 🧮 SQL INSIGHTS

* Queried top-performing products and regions
* Ranked categories using `RANK()` and `ROW_NUMBER()` functions
* Analyzed gross margin percentages per product
* Used conditional logic to classify product sales into High/Medium/Low
* Performed sales trend comparison and regional performance analysis

### 📌 SAMPLE QUERIES

```sql
-- Year-over-Year Growth
SELECT
  Category,
  ROUND((2024_Net_Sales - 2023_Net_Sales)*100/2023_Net_Sales, 2) AS Growth_2024_vs_2023
FROM Net_Sales_By_Product_And_Service;

-- Top 3 Products by 2023 Sales
SELECT Category, 2023_Net_Sales
FROM Net_Sales_By_Product_And_Service
ORDER BY 2023_Net_Sales DESC
LIMIT 3;
```

---

## 📈 POWER BI DASHBOARD

* **Page 1: Product Profitability Overview**

  * Bar chart: Product vs Net Sales (2024)
  * Bar chart: Product vs Gross Margin
  * Matrix: Product, Net Sales, Gross Margin

* **Page 2: Sales Trends (2022–2024)**

  * Line chart: Category-wise trends
  * Stacked bar chart: Category by Year

* **Page 3: Regional Sales Performance**

  * Map visual: Region-wise performance
  * Line chart: Regional trend (2022–2024)

* **Page 4: YoY Sales Growth & KPIs**

  * KPI Cards: Total Sales comparison
  * Manual % Change Labels

* **Page 5: Profitability Ratios & Segment Comparison**

  * Bar and Pie charts for 2024 segment ratios
  * Trendlines and regression predictions

---

## 🧑‍💻 AUTHOR

**ANKUSH KUMAR**
📅 May 2025
🎓 Aspiring Data Analyst | Skilled in Python, SQL & Power BI

---

## 🌐 REPOSITORY STRUCTURE

```
/
|— Python_Analysis_Code.ipynb
|— SQL_Queries.sql
|— PowerBI_Dashboard.pbix
|— datasets/
|     |— Net_Sales_By_Product_And_Service.csv
|     |— Gross_Margin_Values.csv
|     |— Segment_Operating_Performance.csv
|— README.md
```

---

## 🏁 CONCLUSION

This project demonstrates the full data analysis workflow from raw data to impactful storytelling. It reflects an ability to generate insights from multi-source financial data using Python, SQL, and Power BI—a strong portfolio piece for roles in data analytics and business intelligence.

---

> ⭐ If you found this project useful, feel free to star and fork the repo!
