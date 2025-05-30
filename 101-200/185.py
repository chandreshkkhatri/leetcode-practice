import sqlite3
from pathlib import Path
import pandas as pd

DB_FILE = Path('Employee.db')

data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [
    4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
    {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype(
    {'id': 'Int64', 'name': 'object'})


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

        print("Creating 'Department' table and inserting data with Pandas...")
        department.to_sql(
            'Department',       # Table name
            conn,               # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False         # Do not write DataFrame index as a column
        )
        print("Table 'Department' created and populated.")
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
            SELECT d.name as Department, drk_e.name as Employee, drk_e.salary as salary
            FROM
            (SELECT *, DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as drk
            FROM Employee e) drk_e
            JOIN department d
            ON drk_e.departmentId = d.id
            WHERE drk_e.drk <= 3
        ''')
        results = cursor.fetchall()
        for employee, manager in results:
            print(f"Employee: {employee}, Manager: {manager}")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
