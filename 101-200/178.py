import sqlite3
import pandas as pd
from pathlib import Path

DB_FILE = Path('score.db')

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype(
    {'id': 'Int64', 'score': 'Float64'})


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

        print("Creating 'Scores' table and inserting data with Pandas...")
        scores.to_sql(
            'Scores',            # Table name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Scores' created and populated.")
        print("Database setup complete using Pandas.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


def main():
    """
    Write a solution to find rank of the score in the Scores table.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
                        SELECT Score, 
                            DENSE_RANK() OVER(ORDER BY score DESC) as 'rank'
                        FROM Scores
                        ''')

        results = cursor.fetchall()
        for score, rank in results:
            print(f"Score: {score}, Rank: {rank}")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    setup_database_with_pandas()
    main()
    print("Database setup and query execution completed successfully.")
