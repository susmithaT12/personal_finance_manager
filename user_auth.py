import sqlite3

def register_user(username, password):
    """
    Registers a new user by inserting their username and password into the database.
    """
    try:
        connection = sqlite3.connect("personal_finance.db")
        cursor = connection.cursor()

        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("Username already exists.")
            return False

        # Insert new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()

def login_user(username, password):
    """
    Logs in a user by checking their credentials against the database.
    """
    try:
        connection = sqlite3.connect("personal_finance.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        if cursor.fetchone():
            return True
        else:
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()
