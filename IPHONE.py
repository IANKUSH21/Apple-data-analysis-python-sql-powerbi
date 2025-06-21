#!/usr/bin/env python
# coding: utf-8

# 
# #             Apple Inc. Business Analytics Project
# #             Using Python, SQL, and Power BI
# 

# In[48]:


# 🔍 Objective:
# Analyze iPhone sales and Apple’s financial performance using
# Python for data cleaning, SQL for querying, and Power BI for
# interactive dashboards.

# 📊 Tools & Technologies: Python | Pandas | Matplotlib | SQL | Power BI

# 👨‍💻 Author: ANKUSH 
# 📅 Date: MAY 2025


# In[2]:


from IPython.display import Image, display

display(Image(filename=r"C:\Users\ak547\OneDrive\Documents\Downloads\About-Apple-Logo.jpg", width=1200, height=300))


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

NETSALES = pd.read_csv("C:\\SQL PROJECTS ALL\\IPHONE PJ-07\\Net_Sales_By_Product_And_Service.csv")     # duplicate of prod if you wish


# In[4]:


from IPython.display import display


# In[5]:


NETSALES


# In[6]:


GROSS_MARGIN = pd.read_csv("Gross_Margin_Values.csv")  # gross-margin $ values


# In[8]:


SEGMENT = pd.read_csv(r"C:\SQL PROJECTS ALL\IPHONE PJ-07\Segment_Operating_Performance.csv")  # regional net sales


# In[9]:


## 1.The first five rows of each table.
print(" **** NETSALES Data")
display(NETSALES.head())

print(" **** GROSS_MARGIN Data")
display(GROSS_MARGIN.head())

print(" **** SEGMENT Data")
display(SEGMENT.head())


# In[23]:


## 2.How many unique products are listed?
NETSALES['Category'].nunique()


# In[22]:


## 3.Total iPhone net-sales (USD m) across all years.
NETSALES.query("Category == 'iPhone'")[['2024 Net Sales (in $M)', '2023 Net Sales (in $M)', '2022 Net Sales (in $M)']].sum().sum()
print("Total iPhone net-sales (USD m) across all years.")
display(NETSALES.query("Category == 'iPhone'")[['2024 Net Sales (in $M)', '2023 Net Sales (in $M)', '2022 Net Sales (in $M)']].sum().sum())


# In[43]:


## 4. Which region recorded the highest 2024 net-sales?
# Grouping and calculating total sales per region
region_sales = SEGMENT.groupby('Region')['2024 Net Sales (in $M)'].sum()

# Get region with highest sales
top_region = region_sales.idxmax()

# Get the highest sales amount
top_sales = region_sales.max()

# Print result
print(f"The region with the highest 2024 net sales is {top_region} with ${top_sales}.")




# In[59]:


## 5. Sort NETSALES by 2024 sales descending.

NETSALES = NETSALES.sort_values(by=['Category','2024 Net Sales (in $M)'],  ascending=False)
print(f"NETSALES by 2024 sales descending >>>")
display(NETSALES)


# In[69]:


## 6. Mean gross margin in 2024.
MEAN_MARGIN = GROSS_MARGIN['2024 (in $M)'].mean()
print(f"mean gross margin for 2024 is ${MEAN_MARGIN}.")


# In[84]:


## 7. Minimum gross margin across years.
minimum_margin = GROSS_MARGIN[['2024 (in $M)',	'2023 (in $M)','2022 (in $M)']].min()
print(f"Minimum margin for 2024 is {minimum_margin['2024 (in $M)']}, "
      f"minimum margin for 2023 is {minimum_margin['2023 (in $M)']}, "
      f"and minimum margin for 2022 is {minimum_margin['2022 (in $M)']}.")



# In[85]:


## 8. bar chart of 2024 sales by product.
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# In[86]:


NETSALES


# In[102]:


plt.bar(NETSALES['Category'], NETSALES['2024 Net Sales (in $M)'], color = 'steelblue')

plt.xlabel("PRODUCTS",fontsize=12)
plt.ylabel("NET SALES",fontsize=12)
plt.title("SALES OF 2024",fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.2)
plt.xticks(rotation = 45, ha= 'center')



plt.tight_layout()
plt.show()


# In[106]:


## 9.Add a new column for average sales.

NETSALES['AVERAGE SALES'] = NETSALES[["2024 Net Sales (in $M)", "2023 Net Sales (in $M)",	"2022 Net Sales (in $M)"]].mean(axis = 1)
display(NETSALES)         


# In[119]:


## 10 Bar chart for the Average sales 
import seaborn as sns

plt.figure(figsize=(10, 6))
plt.bar(NETSALES["Category"], NETSALES["AVERAGE SALES"], color = colors)
colors = sns.color_palette("pastel", len(NETSALES))


plt.xlabel("Category")
plt.ylabel("Average Sales (in $M)")
plt.title("Average Net Sales by Product Category (2022–2024)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[129]:


## 11. Calculate YoY growth for each year.
NETSALES['2023 YoY Growth'] = (NETSALES['2023 Net Sales (in $M)'] - NETSALES['2022 Net Sales (in $M)']) / NETSALES['2022 Net Sales (in $M)'] * 100
NETSALES['2024 YoY Growth'] = (NETSALES['2024 Net Sales (in $M)'] - NETSALES['2023 Net Sales (in $M)']) / NETSALES['2023 Net Sales (in $M)'] * 100
display(NETSALES)


# In[143]:


## 12 .Compare regional sales in a line chart.
plt.figure(figsize=(10, 6))
SEGMENT.set_index("Region")[["2024 Net Sales (in $M)", "2023 Net Sales (in $M)", "2022 Net Sales (in $M)",]].T.plot()

plt.title("Net Sales by Region (2022–2024)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Net Sales (in $M)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()


# In[180]:


## 13. Top 1 gross margin category
TOP_MARGIN = GROSS_MARGIN.sort_values(["Category"],ascending=True).head(1)
print(f"Top 1 gross margin category is")
display(TOP_MARGIN)


# In[186]:


## 14. Plot pie chart for 2024 regional distribution.

SEGMENT.set_index('Region')['2024 Net Sales (in $M)'].plot.pie(startangle=90,
                                                               shadow=True,)
plt.title("2024 Net Sales by Region", fontsize=14)
plt.xticks(ha= 'center')
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



# In[187]:


## 15. Create a pivot table of net sales by category and year.
pd.pivot_table(NETSALES, values=['2022 Net Sales (in $M)', '2023 Net Sales (in $M)', '2024 Net Sales (in $M)'], index='Category')


# In[188]:


## 16. Identify categories with increasing sales trend.

NETSALES[(NETSALES['2024 Net Sales (in $M)'] > NETSALES['2023 Net Sales (in $M)']) & 
         (NETSALES['2023 Net Sales (in $M)'] > NETSALES['2022 Net Sales (in $M)'])]


# In[190]:


## 17. Find correlation between yearly net sales.
NETSALES[['2022 Net Sales (in $M)', '2023 Net Sales (in $M)', '2024 Net Sales (in $M)']].corr()


# In[7]:


## 18. Group NETSALES by category and sum.
NETSALES.groupby("Category")[["2022 Net Sales (in $M)",	"2023 Net Sales (in $M)", "2024 Net Sales (in $M)"]].sum()


# In[9]:


SEGMENT


# In[13]:


## 19. Create a stacked bar chart for regional sales.
SEGMENT.set_index('Region')[['2024 Net Sales (in $M)', '2023 Net Sales (in $M)', '2022 Net Sales (in $M)']].plot(kind='bar', stacked=True)

plt.title('Net Sales by Region (2022–2024)', fontsize=14)
plt.xlabel('Region')
plt.ylabel('Net Sales (in $M)')
plt.xticks(rotation=45)
plt.legend(title='Year')
plt.tight_layout()
plt.show()


# In[22]:


## 20. plt.scatter
plt.scatter(NETSALES['2023 Net Sales (in $M)'], NETSALES['2024 Net Sales (in $M)'])

plt.xlabel("2023 Net Sales (in $M)")
plt.ylabel("2024 Net Sales (in $M)")
plt.title("2023 vs 2024 Net Sales with Trendline")
plt.grid(True,alpha = 0.2)
plt.legend()


plt.tight_layout()
plt.show()



# In[25]:


## 21. Build a linear regression to predict 2024 sales from 2022 & 2023.

from sklearn.linear_model import LinearRegression
X = NETSALES[['2022 Net Sales (in $M)', '2023 Net Sales (in $M)']]
y = NETSALES['2024 Net Sales (in $M)']
model = LinearRegression().fit(X, y)

coef_2022 = model.coef_[0]
coef_2023 = model.coef_[1]
intercept = model.intercept_

# Print results clearly
print(f"{coef_2022:.3f} (Coefficient for 2022 Net Sales)")
print(f"{coef_2023:.3f} (Coefficient for 2023 Net Sales)")
print(f"{intercept:.2f} (Intercept)")




# In[26]:


## 22. Plot regression predictions vs actuals.
pred = model.predict(X)
plt.scatter(y, pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")


# In[28]:


## 22. Create KPI dashboard using Plotly.

import plotly.express as px
px.bar(
    NETSALES,
    x='Category',
    y='2024 Net Sales (in $M)',
    color='Category',
    title='2024 Net Sales by Category',
    labels={'Category': 'Product Category', '2024 Net Sales (in $M)': 'Net Sales ($M)'}
)


# In[10]:


NETSALES


# In[51]:


## 23. Calculate the ratio of 2024 products net sales to total net sales in 2024

# A. Iphone sale ratio to net sales 2024
Iphone_sales = NETSALES.loc[NETSALES["Category"] == 'iPhone', '2024 Net Sales (in $M)'].values[0] 
Total_sales_2024 = NETSALES["2024 Net Sales (in $M)"].sum()
Ratio_Iphone = Iphone_sales/Total_sales_2024

# B. Mac sales ratio to net sales 2024
Mac_sales = NETSALES.loc[NETSALES["Category"] == "Mac",'2024 Net Sales (in $M)'].values[0]
Ratio_Mac = Mac_sales/Total_sales_2024

## C. Wearables, Home and Accessories sale ratio to net sales 2024
Wearables_H_A_sales = NETSALES.loc[NETSALES["Category"] == "Wearables, Home and Accessories", '2024 Net Sales (in $M)'].values[0]
Ratio_W_H_A = Wearables_H_A_sales/Total_sales_2024

## D. Services sales ratio to net sales 2024
Services_sales  = NETSALES.loc[NETSALES["Category"] == "Services", '2024 Net Sales (in $M)'].values[0]
Ratio_services = Services_sales/Total_sales_2024

print(" 2024 Net Sales Ratios")
print("----------------------------")
print(f" * iPhone                          : {Ratio_Iphone:.2%}")
print(f" * Mac                             : {Ratio_Mac:.2%}")
print(f" * Wearables, Home & Accessories   : {Ratio_W_H_A:.2%}")
print(f" * Services                        : {Ratio_services:.2%}")



# In[61]:


## 24. 
import matplotlib.pyplot as plt

labels = ["iPhone", "Mac", "Wearables, Home & Accessories", "Services"]
values = [Ratio_Iphone, Ratio_Mac, Ratio_W_H_A, Ratio_services]

plt.figure(figsize=(6,4))
colors = ["Red", "Darkblue", "pink", "seagreen"]
plt.bar(labels, values, color=colors)



plt.xlabel("Products")
plt.ylabel("Share of 2024 Net Sales")
plt.title("Ratios of products net sales to total net sales in 2024")
plt.xticks(rotation=15, ha='right')

plt.tight_layout()
plt.show()


# In[70]:


## 25.Calculate ratio of 2024 net sales of 'iPhone' to total segment sales in Americas region

iphone_sales_2024 = NETSALES.loc[NETSALES['Category'] == 'iPhone', '2024 Net Sales (in $M)'].values[0]
americas_sales_2024 = SEGMENT.loc[SEGMENT['Region'] == 'Americas', '2024 Net Sales (in $M)'].values[0]
ratio_iphone_americas = iphone_sales_2024 / americas_sales_2024

print(f"  Ratio of 2024 net sales of 'iPhone' to total segment sales in Americas region    :  {ratio_iphone_americas :.2%}")


# In[93]:


SEGMENT


# In[95]:


## 27. Calculate ratio of total sales in Asia-Pacific segment to total sales across all segments (2024)

# Assuming apac_sales is filtered like this:
apac_sales = SEGMENT.loc[SEGMENT['Region'] == 'Rest of Asia Pacific', '2024 Net Sales (in $M)'].sum()

total_segment_sales = SEGMENT['2024 Net Sales (in $M)'].sum()
apac_ratio = apac_sales / total_segment_sales

# Now apac_ratio is a scalar (float), so this works:
print(f"Ratio of total sales in Asia-Pacific segment to total sales across all segments (2024): {apac_ratio:.2%}")


# In[113]:


## 28. Calculate ratio of 'Services' segment gross margin to total gross margin (2024)

services_margin = GROSS_MARGIN.loc[GROSS_MARGIN['Category'] == 'Services Gross Margin', '2024 (in $M)'].values[0]
total_margin_avg = GROSS_MARGIN['2024 (in $M)'].mean()
ratio_services_to_total = services_margin / total_margin_avg

print(f" Ratio of 'Services' segment gross margin to total gross margin (2024) : {ratio_services_to_total:.2%}")


# In[116]:


## 29. Calculate the ratio of net sales in the highest performing segment to the lowest in 2024.

max_sales = SEGMENT['2024 Net Sales (in $M)'].max()
min_sales = SEGMENT['2024 Net Sales (in $M)'].min()
segment_sales_ratio = max_sales / min_sales

print(f" Ratio of net sales in the highest performing segment to the lowest in 2024 : {segment_sales_ratio:.2%}")


# In[128]:


## 30. Calculate the ratio of average net sales of each product to the overall average across all products.

NETSALES['Product_Avg_Sales'] = NETSALES[
    ['2022 Net Sales (in $M)', '2023 Net Sales (in $M)', '2024 Net Sales (in $M)']].mean(axis=1)

overall_avg = NETSALES['Product_Avg_Sales'].mean()

NETSALES['Relative_Sales_Ratio'] = NETSALES['Product_Avg_Sales'] / overall_avg

display(NETSALES['Relative_Sales_Ratio'])


# In[ ]:




