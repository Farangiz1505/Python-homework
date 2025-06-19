
Homework 1

import pandas as pd
import numpy as np  # Random qiymatlar uchun kerak bo'ladi

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Column nomlarini funksiyadan foydalangan holda o'zgartirish
df.columns = df.columns.str.lower().str.replace(" ", "_")  # umumiy funksiyaviy usul

# 2. Dastlabki 3 qatorni chiqarish
print("First 3 rows:")
print(df.head(3))

# 3. O'rtacha yoshni topish
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# 4. faqat 'first_name' va 'city' ustunlarini tanlash
print("\nSelected columns (first_name and city):")
print(df[['first_name', 'city']])

# 5. Yangi 'salary' ustunini qo'shish (tasodifiy qiymatlar bilan)
df['salary'] = np.random.randint(4000, 7000, size=len(df))

# 6. DataFrame uchun statistik ma'lumotlar
print("\nSummary statistics:")
print(df.describe())


⸻

 Homework 2

# 1. DataFrame yaratish
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# 2. Maksimal qiymatlar
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# 3. Minimal qiymatlar
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# 4. O'rtacha qiymatlar
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())


⸻

Homework 3

# 1. DataFrame yaratish
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)

# 'Category' ustunini indeksga aylantirish
expenses = expenses.set_index('Category')

# 2. Har bir kategoriya uchun maksimal xarajat
print("Max expense per category:")
print(expenses.max(axis=1))

# 3. Har bir kategoriya uchun minimal xarajat
print("\nMin expense per category:")
print(expenses.min(axis=1))

# 4. Har bir kategoriya uchun o'rtacha xarajat
print("\nAverage expense per category:")
print(expenses.mean(axis=1))
