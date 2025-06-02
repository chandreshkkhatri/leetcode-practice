import sqlite3
import pandas as pd
from pathlib import Path

DB_FILE = Path('person.db')

data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype(
    {'id': 'int64', 'email': 'object'})


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

        print("Creating 'Person' table and inserting data with Pandas...")
        person.to_sql(
            'Person',            # Table name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Person' created and populated.")
        print("Database setup complete using Pandas.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


def main():
    """
    Connects to the SQLite database and removes duplicate entries in the Person table.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        # Create the Person table if it doesn't exist
        cursor.execute('''
            DELETE 
            FROM Person 
            WHERE id NOT IN (SELECT * FROM (
                SELECT min(id)
                FROM person
                GROUP BY email) as p)
        ''')
        print("Duplicate entries removed from the Person table.")

        # Print remaining entries
        cursor.execute('SELECT * FROM Person')
        rows = cursor.fetchall()
        print("Remaining entries in the Person table:")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
