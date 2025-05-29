import sqlite3
import pandas as pd
from pathlib import Path

DB_FILE = Path('employees.db')

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4],
        [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype(
    {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'})


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

        print("Creating 'Employee' table and inserting data with Pandas...")
        employee.to_sql(
            'Employee',          # Table name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Employee' created and populated.")
        print("Database setup complete using Pandas.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


def main():
    """
    Write a solution to find the second highest salary from the Employee table.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT e.name as Employee
            FROM employee e, employee m
            WHERE e.managerId = m.id and e.salary>m.salary
            ''')
        results = cursor.fetchall()
        for (employee_name,) in results:
            print(employee_name)
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
