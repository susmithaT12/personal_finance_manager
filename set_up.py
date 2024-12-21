import sqlite3
import shutil

# Backup the database
def backup_database():
    try:
        shutil.copy('finance_app.db', 'finance_app_backup.db')
        print("Backup created as finance_app_backup.db.")
    except FileNotFoundError:
        print("No existing database found to back up.")

# Restore the database from the backup
def restore_database():
    try:
        shutil.copy('finance_app_backup.db', 'finance_app.db')
        print("Database restored from finance_app_backup.db.")
    except FileNotFoundError:
        print("Backup file not found. Cannot restore the database.")

# Create tables for transactions, budgets, and users
def create_tables():
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')

    # Create budgets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            budget_amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Tables created successfully.")

# Run the script to create tables
if __name__ == "__main__":
    # Ensure database tables are set up
    create_tables()

    # Create a backup of the database
    backup_database()

