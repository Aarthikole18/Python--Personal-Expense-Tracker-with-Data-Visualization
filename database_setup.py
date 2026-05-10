# =========================================
# SQLITE DATABASE SETUP
# PERSONAL EXPENSE TRACKER
# =========================================

import sqlite3
import pandas as pd
import os

# =========================================
# CREATE DB FOLDER IF NOT EXISTS
# =========================================

os.makedirs("db", exist_ok=True)

# =========================================
# CONNECT DATABASE
# =========================================

connection = sqlite3.connect("db/expense_tracker.db")

cursor = connection.cursor()

# =========================================
# CREATE TABLE
# =========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    Date TEXT,

    Category TEXT,

    Amount REAL,

    Payment_Method TEXT,

    Description TEXT

)
""")

print("Database table created successfully!")

# =========================================
# LOAD CSV DATA
# =========================================

df = pd.read_csv("outputs/cleaned_expense_data.csv")

# =========================================
# INSERT DATA INTO DATABASE
# =========================================

df.to_sql(
    "expenses",
    connection,
    if_exists="replace",
    index=False
)

print("Expense data inserted into database successfully!")

# =========================================
# VERIFY DATA
# =========================================

query = "SELECT * FROM expenses LIMIT 5"

result = pd.read_sql(query, connection)

print("\nFirst 5 Rows From Database:\n")

print(result)

# =========================================
# CLOSE CONNECTION
# =========================================

connection.close()

print("\nDatabase connection closed!")