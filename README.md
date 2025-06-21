# APPLE INC. BUSINESS ANALYTICS PROJECT

🔍 Objective
To analyze Apple Inc.’s product performance—specifically iPhone sales—and assess revenue growth, gross margins, and regional sales trends across 2022 to 2024 using Python, SQL, and Power BI. This project demonstrates my ability to blend technical skills with business insight for data-driven storytelling.

🚀 Key Outcomes
📊 Identified top-performing products and sales categories.

🌍 Analyzed regional net sales trends and growth patterns.

💰 Compared gross margins across service and product categories.

🧠 Built sales forecasts using regression in Python.

📈 Created a dynamic and visually engaging Power BI dashboard.

🧰 Tools & Technologies
Tool	Usage
Python 🐍	Data cleaning, preprocessing, exploratory analysis
SQL 🧾	Structured querying, aggregation, growth & trend insights
Power BI 📊	Dashboards with filters, time-trend analysis, KPI visuals

📂 Dataset Overview
Used three major datasets:

Net_Sales_By_Product_And_Service.csv – Sales of Apple products (2022–2024)

Gross_Margin_Values.csv – Gross margins for services and products

Segment_Operating_Performance.csv – Regional sales performance

📌 Python Analysis Highlights
python
Copy
Edit
# Total iPhone Net Sales across 3 years:
607,255 million USD

# Region with highest 2024 Net Sales:
🌎 Americas: $167,045 million

# Average Gross Margin (2024):
💰 $120,455 million

# Linear Regression for 2024 Sales Forecast:
- Coefficients: [-0.449 (2022), 1.486 (2023)]
- Intercept: -1898.15
📉 Visualizations Created in Python:
📈 Line charts: Yearly trends by region

📊 Bar charts: Product-wise 2024 and average sales

🧮 Pie charts: Regional distribution of 2024 sales

🧪 Scatter plots with regression predictions

Used matplotlib, seaborn, plotly, sklearn

💾 SQL Query Highlights
✔️ Top insights extracted via SQL:

Top 5 products by net sales in 2023

YOY growth (%) across all products

CASE-based sales categorization (High / Medium / Low)

Gross margin % by product

Regional performance comparison

Ranking with RANK() and filtering with HAVING, CASE, and WINDOW functions


-- Calculate YoY Growth
SELECT Category,
ROUND((2023_Net_Sales - 2022_Net_Sales)*100 / 2022_Net_Sales, 2) AS Growth_2023_vs_2022,
ROUND((2024_Net_Sales - 2023_Net_Sales)*100 / 2023_Net_Sales, 2) AS Growth_2024_vs_2023
FROM net_sales_by_product_and_service;
📊 Power BI Dashboard
📌 Pages Designed (No DAX Used)
Product Profitability Overview
→ Bar Charts, Matrix, KPIs

Category-wise Sales Trends (2022–2024)
→ Line chart, Stacked bars, Slicers

Regional Sales Performance
→ Map visual, bar chart, matrix

Year-over-Year Growth Dashboard
→ Line chart, KPI cards, % change analysis

Sales Contribution & Comparative Ratios
→ Pie charts, cards, bar plots

⚡ All visuals are interactive, responsive, and filterable by product, year, and region.

🌟 Key Business Insights
iPhone remains the top revenue generator contributing over 26% to total sales in 2024.

Services have shown continuous growth from 2022 to 2024 with increasing gross margins.

The Americas dominate in regional sales performance.

Products like Mac and iPad show declining trends, calling for product innovation strategy review.

Regression model identifies strong dependence on recent year trends for sales prediction.

📸 Dashboard Preview

👨‍💻 About the Author
Ankush Kumar | Data Analyst & Power BI Enthusiast
💼 Proficient in SQL, Python, Financial Modeling, and Microsoft Dynamics 365
📍 Aspiring to create impact through data-driven insights
📧 [ak547874@gmail.com]
🔗 LinkedIn

📁 How to Use This Repo
bash
Copy
Edit
git clone https://github.com/yourusername/apple-sales-analytics
cd apple-sales-analytics
# Open Power BI dashboard .pbix file
# View Python notebooks or run SQL scripts as needed
