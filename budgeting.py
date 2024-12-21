import sqlite3

def set_budget(category, amount):
    """
    Sets a budget for a specific category.
    """
    try:
        connection = sqlite3.connect("personal_finance.db")
        cursor = connection.cursor()

        # Insert or update the budget for the category
        cursor.execute("INSERT OR REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category, amount))
        connection.commit()
        print(f"Budget set for {category}: {amount}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def view_budget():
    """
    Views all budgets set for different categories.
    """
    try:
        connection = sqlite3.connect("personal_finance.db")
        cursor = connection.cursor()

        cursor.execute("SELECT category, amount FROM budgets")
        budgets = cursor.fetchall()
        if budgets:
            print("Budgets:")
            for category, amount in budgets:
                print(f"{category}: {amount}")
        else:
            print("No budgets set.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()
