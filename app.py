# =========================================
# STREAMLIT DASHBOARD
# PERSONAL EXPENSE TRACKER
# =========================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Personal Expense Tracker",
    layout="wide"
)

st.title("💸 Personal Expense Tracker Dashboard")

# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv("outputs/cleaned_expense_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

# =========================================
# SIDEBAR FILTER
# =========================================

st.sidebar.header("📂 Filter Expenses")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category_filter)]

# =========================================
# METRICS SECTION
# =========================================

total_spending = filtered_df["Amount"].sum()

average_spending = filtered_df["Amount"].mean()

highest_category = (
    filtered_df.groupby("Category")["Amount"]
    .sum()
    .idxmax()
)

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Spending", f"₹{total_spending:,.0f}")

col2.metric("📊 Average Expense", f"₹{average_spending:,.0f}")

col3.metric("🔥 Top Category", highest_category)

st.divider()

# =========================================
# CATEGORY-WISE BAR CHART
# =========================================

col4, col5 = st.columns(2)

with col4:

    st.subheader("📊 Category Spending")

    category_analysis = (
        filtered_df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    fig1, ax1 = plt.subplots(figsize=(5, 3))

    category_analysis.plot(
        kind="bar",
        ax=ax1
    )

    ax1.set_xlabel("Category")
    ax1.set_ylabel("Amount")

    plt.xticks(rotation=45)

    st.pyplot(fig1)

# =========================================
# PAYMENT METHOD PIE CHART
# =========================================

with col5:

    st.subheader("💳 Payment Methods")

    payment_analysis = (
        filtered_df.groupby("Payment_Method")["Amount"]
        .sum()
    )

    fig2, ax2 = plt.subplots(figsize=(4, 4))

    payment_analysis.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax2
    )

    ax2.set_ylabel("")

    st.pyplot(fig2)

st.divider()

# =========================================
# MONTHLY SPENDING TREND
# =========================================

st.subheader("📈 Monthly Spending Trend")

filtered_df["Month"] = (
    filtered_df["Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_analysis = (
    filtered_df.groupby("Month")["Amount"]
    .sum()
)

fig3, ax3 = plt.subplots(figsize=(8, 3))

monthly_analysis.plot(
    kind="line",
    marker="o",
    ax=ax3
)

ax3.set_xlabel("Month")
ax3.set_ylabel("Amount")

st.pyplot(fig3)

# =========================================
# DAILY SPENDING TREND
# =========================================

st.subheader("📅 Daily Spending Trend")

daily_spending = (
    filtered_df.groupby("Date")["Amount"]
    .sum()
)

fig4, ax4 = plt.subplots(figsize=(8, 3))

daily_spending.plot(
    kind="line",
    color="red",
    ax=ax4
)

ax4.set_xlabel("Date")
ax4.set_ylabel("Amount")

st.pyplot(fig4)

st.divider()

# =========================================
# DATAFRAME
# =========================================

st.subheader("📄 Expense Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=300
)

# =========================================
# DOWNLOAD BUTTON
# =========================================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="filtered_expense_data.csv",
    mime="text/csv"
)

st.success("Dashboard Loaded Successfully!")