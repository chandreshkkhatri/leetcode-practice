import sqlite3
from pathlib import Path
import pandas as pd

DB_FILE = Path('Employee.db')

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [
    3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
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
            SELECT d.name as Department, e3.name as Employee, e3.salary as Salary
            FROM Department d INNER JOIN
            (SELECT e1.name, e1.salary, e1.departmentid FROM employee e1
            JOIN (SELECT e.name, max(e.salary) as salary, e.DepartmentId FROM Employee e
                GROUP BY DepartmentId) e2
            WHERE e1.salary=e2.salary and e1.departmentId=e2.departmentId and e1.salary is not null) e3
                ON d.id = e3.DepartmentId
            ''')

        results = cursor.fetchall()
        for (department, employee, salary) in results:
            print(f"{department} {employee} {salary}")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
