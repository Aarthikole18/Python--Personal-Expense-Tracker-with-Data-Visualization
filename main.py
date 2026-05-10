# =========================================
# PERSONAL EXPENSE TRACKER PROJECT
# =========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import random
import os

# =========================================
# CREATE REQUIRED FOLDERS
# =========================================

folders = ["data", "outputs", "images", "reports"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# =========================================
# STEP 1: CREATE SYNTHETIC EXPENSE DATA
# =========================================

categories = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Healthcare",
    "Education"
]

payment_methods = [
    "Cash",
    "UPI",
    "Credit Card",
    "Debit Card"
]

descriptions = [
    "Restaurant",
    "Uber Ride",
    "Amazon Purchase",
    "Electricity Bill",
    "Movie Ticket",
    "Medical Store",
    "Books Purchase"
]

data = []

for i in range(200):

    expense_date = pd.Timestamp("2025-01-01") + pd.to_timedelta(
        random.randint(0, 120),
        unit='D'
    )

    category = random.choice(categories)

    amount = random.randint(100, 5000)

    payment = random.choice(payment_methods)

    description = random.choice(descriptions)

    data.append([
        expense_date,
        category,
        amount,
        payment,
        description
    ])

expense_df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Category",
        "Amount",
        "Payment_Method",
        "Description"
    ]
)

expense_df.to_csv(
    "data/expense_data.csv",
    index=False
)

print("Expense dataset created successfully!")

# =========================================
# STEP 2: LOAD DATA
# =========================================

df = pd.read_csv("data/expense_data.csv")

print("\nFirst 5 Rows:")
print(df.head())

# =========================================
# STEP 3: DATA CLEANING
# =========================================

df.dropna(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M")

print("\nData cleaned successfully!")

# =========================================
# STEP 4: CATEGORY-WISE ANALYSIS
# =========================================

category_analysis = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Spending:")
print(category_analysis)

highest_category = category_analysis.idxmax()

print(f"\nHighest Spending Category: {highest_category}")

# =========================================
# STEP 5: MONTHLY ANALYSIS
# =========================================

monthly_analysis = (
    df.groupby("Month")["Amount"]
    .sum()
)

print("\nMonthly Spending:")
print(monthly_analysis)

# =========================================
# STEP 6: PAYMENT METHOD ANALYSIS
# =========================================

payment_analysis = (
    df.groupby("Payment_Method")["Amount"]
    .sum()
)

print("\nPayment Method Analysis:")
print(payment_analysis)

# =========================================
# STEP 7: DAILY SPENDING ANALYSIS
# =========================================

daily_spending = (
    df.groupby("Date")["Amount"]
    .sum()
)

average_daily_spending = daily_spending.mean()

print(f"\nAverage Daily Spending: ₹{average_daily_spending:.2f}")

# =========================================
# STEP 8: VISUALIZATIONS
# =========================================

sns.set_style("whitegrid")

# CATEGORY BAR CHART
plt.figure(figsize=(10, 5))

category_analysis.plot(
    kind="bar",
    color="skyblue"
)

plt.title("Category-wise Spending")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig(
    "images/category_spending_bar_chart.png"
)

plt.close()

# MONTHLY LINE CHART
plt.figure(figsize=(10, 5))

monthly_analysis.plot(
    kind="line",
    marker="o",
    color="green"
)

plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig(
    "images/monthly_spending_line_chart.png"
)

plt.close()

# PAYMENT METHOD PIE CHART
plt.figure(figsize=(8, 8))

payment_analysis.plot(
    kind="pie",
    autopct='%1.1f%%'
)

plt.ylabel("")

plt.title("Payment Method Distribution")

plt.tight_layout()

plt.savefig(
    "images/payment_method_pie_chart.png"
)

plt.close()

# DAILY SPENDING TREND
plt.figure(figsize=(12, 5))

daily_spending.plot(
    kind="line",
    color="red"
)

plt.title("Daily Spending Trend")
plt.xlabel("Date")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig(
    "images/daily_spending_trend_chart.png"
)

plt.close()

print("\nCharts saved successfully!")

# =========================================
# STEP 9: REPORT GENERATION
# =========================================

report = {
    "Total Spending": [df["Amount"].sum()],
    "Average Daily Spending": [average_daily_spending],
    "Highest Spending Category": [highest_category]
}

report_df = pd.DataFrame(report)

report_df.to_csv(
    "reports/final_expense_report.csv",
    index=False
)

print("\nFinal report generated successfully!")

# =========================================
# STEP 10: SAVE CLEANED DATA
# =========================================

df.to_csv(
    "outputs/cleaned_expense_data.csv",
    index=False
)

print("\nProject execution completed successfully!")