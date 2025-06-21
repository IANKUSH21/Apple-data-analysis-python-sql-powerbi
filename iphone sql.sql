CREATE DATABASE Iphone;

USE Iphone;

CREATE TABLE Net_Sales_By_Product_And_Service
(Category VARCHAR (50) PRIMARY KEY,
 2024_Net_Sales  INT,
 2023_Net_Sales  INT,
 2022_Net_Sales INT);
 
 DELETE FROM Net_Sales_By_Product_And_Service
WHERE Category = 'Total';

SELECT * FROM Net_Sales_By_Product_And_Service;

CREATE TABLE gross_margin_data (
Product VARCHAR (50),
Gross_Margin INT,
Net_Sales 	INT);

SELECT * FROM gross_margin_data;

CREATE TABLE  Segment_Operating_Performance ( 
Region VARCHAR (50),
2024_Net_Sales INT,
2023_Net_Sales INT,
2022_Net_Sales INT);

SET SQL_SAFE_UPDATES = 0;

DELETE FROM Segment_Operating_Performance
WHERE Region = 'Total';


SELECT * FROM  Segment_Operating_Performance ;

--- List all products with net sales greater than 100 million in 2024. 

SELECT Category, 2024_Net_Sales
FROM Net_Sales_By_Product_And_Service
WHERE 2024_Net_Sales >= 100000
GROUP BY Category, 2024_Net_Sales;

-- Show distinct regions available in the SEGMENT dataset.

SELECT Region, COUNT(*) AS occurrences
FROM segment_operating_performance
GROUP BY Region;

-- Find the average gross margin percentage by product in GROSS_MARGIN

SELECT Product,
AVG(Gross_Margin/Net_Sales * 100) AS GROSS_MARGIN_PERCENTAGE
FROM gross_margin_data
GROUP BY Product;

-- List the top 5 products by net sales in 2023.

SELECT Category,2023_Net_Sales
FROM net_sales_by_product_and_service
GROUP BY Category
ORDER BY 2023_Net_Sales DESC
LIMIT 5;


-- Find products whose net sales increased from 2022 to 2024 (compare columns).

SELECT 
  Category,
  2024_Net_Sales,
  2023_Net_Sales,
  2022_Net_Sales
FROM net_sales_by_product_and_service
WHERE 2024_Net_Sales > 2023_Net_Sales
  AND 2023_Net_Sales > 2022_Net_Sales
ORDER BY 2024_Net_Sales DESC;

-- Find the region with the highest total net sales in SEGMENT in 2024 .

SELECT max(2024_Net_Sales), Region
FROM segment_operating_performance
GROUP BY Region
LIMIT 1;

-- Show the sum of net sales grouped by category in NETSALES.

SELECT 
    Category, 
    SUM(2024_Net_Sales + 2023_Net_Sales + 2022_Net_Sales) AS Total_Sales
FROM 
    net_sales_by_product_and_service
GROUP BY 
    Category
ORDER BY Total_Sales DESC;

-- Retrieve all rows from NETSALES where Category is ‘iPhone’.

SELECT *
FROM net_sales_by_product_and_service
WHERE Category = 'Iphone';

-- List the top 3 products by net sales in 2023.

SELECT Category, 
2023_Net_Sales 
FROM net_sales_by_product_and_service
ORDER BY 2023_Net_Sales  DESC
LIMIT 3;

-- Find the yearly percentage growth of net sales for each product.

SELECT 
Category,
2024_Net_Sales,
2023_Net_Sales,
2022_Net_Sales,

ROUND((2023_Net_Sales - 2022_Net_Sales ) * 100 / 2022_Net_Sales,2 ) AS Growth_2023_vs_2022,
ROUND((2024_Net_Sales - 2023_Net_Sales ) * 100 / 2023_Net_Sales, 2) AS Growth_2024_vs_2023

FROM net_sales_by_product_and_service;

-- Use CASE statements to categorize products by net sales volume (High, Medium, Low).

SELECT 
CASE 
WHEN 2024_Net_Sales >= 200000 THEN 'HIGH'
WHEN 2024_Net_Sales >= 100000 THEN 'MEDIUM'
WHEN 2024_Net_Sales >= 50000 THEN 'LOW'
ELSE 'WEAK' 
END AS SALE_CATEGORY,
COUNT(*) AS PRODUCT_COUNT 
FROM net_sales_by_product_and_service 
GROUP BY SALE_CATEGORY;

-- Create a ranking of products based on net sales in 2024 using window functions (ROW_NUMBER or RANK).

SELECT
    Category,
    2024_Net_Sales,
    RANK() OVER (ORDER BY 2024_Net_Sales DESC) AS Sales_Rank
FROM
net_sales_by_product_and_service;

-- List all regions with total 2024 Net Sales above 150000 (in $M).

SELECT Region, 2024_Net_Sales
FROM segment_operating_performance
WHERE 2024_Net_Sales >= 150000
GROUP BY Region, 2024_Net_Sales;

-- Find the region with the highest growth from 2022 to 2024.

SELECT Region,
2024_Net_Sales,
2023_Net_Sales,
2022_Net_Sales,

ROUND((2023_Net_Sales - 2022_Net_Sales) * 100 / 2022_Net_Sales) AS Growth_2023_vs_2022,
ROUND((2024_Net_Sales - 2023_Net_Sales) * 100 / 2023_Net_Sales) AS Growth_2024_vs_2023
FROM
segment_operating_performance
ORDER BY Growth_2023_vs_2022, Growth_2024_vs_2023 DESC
LIMIT 3;

-- List products where 2023 Net Sales decreased compared to 2022

SELECT 
Category,
2023_Net_Sales,
2022_Net_Sales,

ROUND((2023_Net_Sales - 2022_Net_Sales ) * 100 / 2022_Net_Sales,2 ) AS Growth_2023_vs_2022

FROM net_sales_by_product_and_service
ORDER BY Growth_2023_vs_2022 ASC;

-- Find the top 3 products with the highest average Net Sales across 3 years.

SELECT Category,
2024_Net_Sales
2023_Net_Sales,
2022_Net_Sales,
-- AVG CALCULATION --
ROUND((2022_Net_Sales + 2023_Net_Sales + 2024_Net_Sales) / 3.0, 2) AS Avg_Net_Sales

FROM net_sales_by_product_and_service

GROUP BY Category,
2024_Net_Sales,
2023_Net_Sales,
2022_Net_Sales
ORDER BY 
Avg_Net_Sales DESC
LIMIT 3;

-- Show products with 2024 Net Sales greater than 100000

SELECT *
FROM net_sales_by_product_and_service
WHERE 2024_Net_Sales >= 100000;

-- Show percentage growth in Net Sales from 2022 to 2024 for iPhone.

SELECT Category,
2024_Net_Sales,
2023_Net_Sales,
2022_Net_Sales,

ROUND((2023_Net_Sales - 2022_Net_Sales) * 100 / 2022_Net_Sales) AS Growth_2023_vs_2022,
ROUND((2024_Net_Sales - 2023_Net_Sales) * 100 / 2023_Net_Sales) AS Growth_2024_vs_2023
FROM net_sales_by_product_and_service
WHERE Category = 'iPhone';

-- Find the product with the highest 2023 Net Sales.

SELECT Category,
2023_Net_Sales
FROM net_sales_by_product_and_service
ORDER BY 2023_Net_Sales DESC
LIMIT 1;

--  Calculate the contribution (%) of each product’s net sales to the total net sales in 2024.

SELECT 
    Category,
    (2024_Net_Sales),
    ROUND((2024_Net_Sales) * 100.0) / 
          (SELECT SUM(2024_Net_Sales) FROM Net_Sales_By_Product_And_Service), 2 AS Contribution_Percentage
FROM 
    Net_Sales_By_Product_And_Service;

-- Find the standard deviation of 2024 net sales for all products to assess sales volatility.

SELECT 
    STDDEV(2024_Net_Sales) AS Std_Dev_2024_Sales
FROM 
    Net_Sales_By_Product_And_Service




















