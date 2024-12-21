import sqlite3
from datetime import datetime

# Create a connection to the database
def create_connection():
    conn = sqlite3.connect('finance_app.db')
    return conn

# Add a transaction
def add_transaction(user_id, amount, category, transaction_type, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (user_id, amount, category, transaction_type, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, amount, category, transaction_type, description))
    conn.commit()
    conn.close()
    print(f"Transaction added successfully: {amount} - {category} - {transaction_type}")

# View all transactions for a user
def view_transactions(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM transactions WHERE user_id = ?
    ''', (user_id,))
    transactions = cursor.fetchall()
    
    if transactions:
        print("\nTransactions:")
        for txn in transactions:
            print(f"Amount: {txn[1]}, Category: {txn[2]}, Type: {txn[3]}, Description: {txn[4]}")
    else:
        print("No transactions found.")
    
    conn.close()

# Generate a simple report (total income/expense)
import sqlite3

def generate_report(user_id):
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()

    # Fetch all transactions for the given user_id
    cursor.execute('''
        SELECT amount, transaction_type FROM transactions WHERE user_id = ?
    ''', (user_id,))
    transactions = cursor.fetchall()

    # Calculate income, expenses, and savings
    monthly_income = sum(amount for amount, t_type in transactions if t_type == 'Income')
    monthly_expenses = sum(amount for amount, t_type in transactions if t_type == 'Expense')
    monthly_savings = monthly_income - monthly_expenses

    # Print the report
    print("\n--- Financial Report ---")
    print(f"Total Monthly Income: {monthly_income}")
    print(f"Total Monthly Expenses: {monthly_expenses}")
    print(f"Monthly Savings: {monthly_savings}")
    print("------------------------")

    conn.close()


# Set a budget for a user
budgets = {}

def set_budget(user_id, budget_amount):
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()

    # Check if a budget already exists for the user
    cursor.execute('SELECT * FROM budgets WHERE user_id = ?', (user_id,))
    existing_budget = cursor.fetchone()

    if existing_budget:
        # Update the existing budget
        cursor.execute('''
            UPDATE budgets
            SET budget_amount = ?
            WHERE user_id = ?
        ''', (budget_amount, user_id))
        print("Budget updated successfully!")
    else:
        # Insert a new budget record
        cursor.execute('''
            INSERT INTO budgets (user_id, budget_amount)
            VALUES (?, ?)
        ''', (user_id, budget_amount))
        print("Budget set successfully!")

    conn.commit()
    conn.close()

def view_budget(user_id):
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()

    # Fetch the budget for the logged-in user
    cursor.execute('SELECT budget_amount FROM budgets WHERE user_id = ?', (user_id,))
    budget = cursor.fetchone()

    if budget:
        print(f"Your current budget is: {budget[0]}")
    else:
        print("No budget set for your account. Please set a budget first.")

    conn.close()


def update_transaction(user_id, transaction_id):
    print("Update a transaction.")
    # Find the transaction to update
    for transaction in transactions:
        if transaction['transaction_id'] == transaction_id and transaction['user_id'] == user_id:
            transaction['amount'] = float(input("Enter new amount: "))
            transaction['category'] = input("Enter new category: ")
            transaction['description'] = input("Enter new description: ")
            print("Transaction updated successfully!")
            return
    print("Transaction not found!")

def delete_transaction(user_id, transaction_id):
    global transactions
    transactions = [t for t in transactions if not (t['transaction_id'] == transaction_id and t['user_id'] == user_id)]
    print("Transaction deleted successfully!")
