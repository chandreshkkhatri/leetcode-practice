import sqlite3
import pandas as pd
from pathlib import Path

DB_FILE = Path('employee.db')

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype(
    {'Id': 'Int64', 'Salary': 'Int64'})


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
    Find nth highest distinct salary from the Employee table.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
            BEGIN
            declare a int;
            set a=N-1;
            RETURN (
                # Write your MySQL query statement below.
                    SELECT DISTINCT Salary 
                    FROM Employee
                    ORDER BY Salary DESC 
                    LIMIT a, 1
            );
            END
            ''')
        cursor.execute('SELECT getNthHighestSalary(2)')
        result = cursor.fetchone()
        if result and result[0] is not None:
            print(f"Second highest salary: {result[0]}")
        else:
            print("There is no second highest salary.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
    print("Database setup completed successfully.")
