import sqlite3
import pandas as pd
import os


###################### Question setup ##################
DB_FILE = 'leetcode_db.db'

person_data = [[1, 'Wang', 'Allen'], [2, 'Liu', 'John']]
person_df = pd.DataFrame(person_data, columns=['personId', 'lastName', 'firstName']).astype({
    'personId': 'Int64',  # Using Int64 for nullable integer type
    'lastName': 'object',
    'firstName': 'object'
})

address_data = [[1, 2, 'New York City', 'New York'],
                [2, 3, 'Leetcode', 'California']]
address_df = pd.DataFrame(address_data, columns=['addressId', 'personId', 'city', 'state']).astype({
    'addressId': 'Int64',
    'personId': 'Int64',
    'city': 'object',
    'state': 'object'
})


def setup_database_with_pandas():
    """
    Connects to the SQLite database and populates it using Pandas DataFrames.
    """
    conn = None
    try:
        # Remove existing DB file to start fresh if it exists
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
            print(f"Removed existing database file: {DB_FILE}")

        # Connect to the SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        print(f"Connected to database: {DB_FILE}")

        print("Creating 'Person' table and inserting data with Pandas...")
        person_df.to_sql(
            'Person',            # Table name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Person' created and populated.")

        print("Creating 'Address' table and inserting data with Pandas...")
        address_df.to_sql(
            'Address',           # Table name
            conn,                # Database connection
            if_exists='replace',  # Replace table if it already exists
            index=False          # Do not write DataFrame index as a column
        )
        print("Table 'Address' created and populated.")
        print("Database setup complete using Pandas.")

    except sqlite3.Error as e:
        print(f"An SQLite error occurred: {e}")
        if conn:
            conn.rollback()  # Rollback any changes if an error occurred
        print("Database setup failed due to an error.")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


##################### Solution below ########################

def solve_the_problem():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        SELECT p.firstName, p.lastName, a.city, a.state
        FROM Person p 
        LEFT JOIN Address a
        ON p.personId = a.personId;
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    setup_database_with_pandas()
    solve_the_problem()
