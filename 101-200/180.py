import sqlite3
import pandas as pd
import pathlib

DB_FILE = pathlib.Path('logs.db')

data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype(
    {'id': 'Int64', 'num': 'Int64'})


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

        print("Creating 'Logs' table and inserting data with Pandas...")
        logs.to_sql(
            'Logs',              # Table   name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Logs' created and populated.")
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
                SELECT DISTINCT l3.num as ConsecutiveNums FROM Logs l1, Logs l2, Logs l3
                WHERE l1.num = l2.num and l2.num = l3.num and l1.id = l2.id-1 and l2.id=l3.id-1 
                ''')

        results = cursor.fetchall()
        for (consecutive_num,) in results:
            print(consecutive_num)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
