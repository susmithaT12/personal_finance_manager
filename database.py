import sqlite3
from sqlite3 import Error

# Database file name
DATABASE_NAME = "personal_finance.db"

def create_connection():
    """
    Create a database connection to the SQLite database.
    """
    connection = None
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, parameters=None):
    """
    Execute a single query (CREATE, INSERT, UPDATE, DELETE).
    """
    cursor = connection.cursor()
    try:
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query, parameters=None):
    """
    Execute a query to read data (SELECT).
    """
    cursor = connection.cursor()
    result = None
    try:
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    return result

def initialize_database():
    """
    Initialize the database with required tables.
    """
    connection = create_connection()

    # Users table
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """

    # Transactions table
    create_transactions_table = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    # Budget table
    create_budget_table = """
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        category TEXT NOT NULL,
        limit_amount REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    # Execute the table creation queries
    execute_query(connection, create_users_table)
    execute_query(connection, create_transactions_table)
    execute_query(connection, create_budget_table)

    print("Database initialized successfully")
    connection.close()

# Run the script to initialize the database when this file is executed
if __name__ == "__main__":
    initialize_database()
