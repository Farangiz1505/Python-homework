


 Homework Assignment 1: Analyzing Sales Data

Fayl: task/sales_data.csv

 1. Guruhlab quyidagilarni hisoblang:

import pandas as pd

# CSV faylni o‘qish
df = pd.read_csv("task/sales_data.csv")

# 1-Topshiriq
grouped = df.groupby('Category').agg({
    'Quantity': ['sum', 'max'],
    'Price': 'mean'
}).reset_index()

grouped.columns = ['Category', 'Total_Quantity_Sold', 'Max_Quantity_Single', 'Average_Price']
print(grouped)


⸻

 2. Har bir kategoriyada eng ko‘p sotilgan mahsulotni topish:

top_products = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling = top_products.groupby('Category').first().reset_index()
print(top_selling)


⸻

 3. Eng katta umumiy savdo sodir bo‘lgan sanani aniqlang:

df['Total_Sale'] = df['Quantity'] * df['Price']
sales_by_date = df.groupby('Date')['Total_Sale'].sum().reset_index()
max_sales_date = sales_by_date.loc[sales_by_date['Total_Sale'].idxmax()]
print(max_sales_date)


⸻

Homework Assignment 2: Examining Customer Orders

Fayl: task/customer_orders.csv

1. 20 ta buyurtmadan kam qilgan mijozlarni chiqarib tashlang:

df = pd.read_csv("task/customer_orders.csv")

order_counts = df.groupby('CustomerID')['OrderID'].count()
valid_customers = order_counts[order_counts >= 20].index
filtered_df = df[df['CustomerID'].isin(valid_customers)]
print(filtered_df)


⸻

2. O’rtacha mahsulot narxi $120 dan yuqori bo‘lgan mijozlarni aniqlang:

avg_price = df.groupby('CustomerID')['Price'].mean().reset_index()
high_spenders = avg_price[avg_price['Price'] > 120]
print(high_spenders)


⸻

3. Har bir mahsulot uchun umumiy miqdor va umumiy narx, so‘ng miqdori 5 dan kam bo‘lganlarni olib tashlang:

product_stats = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Sales=('Price', lambda x: (x * df.loc[x.index, 'Quantity']).sum())
).reset_index()

filtered_products = product_stats[product_stats['Total_Quantity'] >= 5]
print(filtered_products)


⸻

Homework Assignment 3: Population Salary Analysis

Ma’lumotlar manbai:
	•	SQLite database: task/population.db → population jadvali
	•	Excel fayl: task/population salary analysis.xlsx → salary band kategoriyalarini beradi

 1. Ma’lumotlarni SQL orqali chaqirish:

import sqlite3

conn = sqlite3.connect("task/population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

 2. Exceldan Salary Bandlarni o‘qish va birlashtirish:

salary_band_df = pd.read_excel("task/population salary analysis.xlsx")

# Taxmin qilamizki, bu faylda 'Min', 'Max', 'Band' ustunlari mavjud
def get_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Band']
    return 'Unknown'

population_df['Salary_Band'] = population_df['Salary'].apply(get_salary_band)


⸻

 3. Har bir band uchun statistikalarni hisoblash:

by_band = population_df.groupby('Salary_Band')['Salary'].agg(
    Percentage=lambda x: len(x) / len(population_df) * 100,
    Average='mean',
    Median='median',
    Count='count'
).reset_index()
print(by_band)


⸻

 4. Har bir shtat bo‘yicha xuddi shu hisob-kitoblar:

by_state_band = population_df.groupby(['State', 'Salary_Band'])['Salary'].agg(
    Percentage=lambda x: len(x) / len(population_df) * 100,
    Average='mean',
    Median='median',
    Count='count'
).reset_index()
print(by_state_band)



