import sqlite3
from pathlib import Path
import pandas as pd

DB_FILE = Path('Customer.db')
data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype(
    {'id': 'Int64', 'name': 'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype(
    {'id': 'Int64', 'customerId': 'Int64'})


def setup_database_with_pandas():
    """
    Connects to the SQLite database and populates it using Pandas DataFrames.
    """
    conn = None
    try:
        # Remove existing DB file to start fresh if it exists
        if DB_FILE.exists():
            DB_FILE.unlink()
            print(f"Removed existing database file: {DB_FILE}")

        # Connect to the SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        print(f"Connected to database: {DB_FILE}")

        print("Creating 'Customers' table and inserting data with Pandas...")
        customers.to_sql(
            'Customers',         # Table name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Customers' created and populated.")

        print("Creating 'Orders' table and inserting data with Pandas...")
        orders.to_sql(
            'Orders',           # Table name
            conn,               # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False         # Do not write DataFrame index as a column
        )
        print("Table 'Orders' created and populated.")
        print("Database setup complete using Pandas.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


def main():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT name as customers
            FROM Customers c
            WHERE c.id NOT IN (
                SELECT DISTINCT customerId FROM ORDERS
            )
        ''')
        results = cursor.fetchall()
        for (customer_name,) in results:
            print(customer_name)
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
