import sqlite3
def generate_report(user_id):
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        SUM(CASE WHEN transaction_type = 'income' THEN amount ELSE 0 END) AS total_income,
        SUM(CASE WHEN transaction_type = 'expense' THEN amount ELSE 0 END) AS total_expense
    FROM transactions WHERE user_id = ?
    """, (user_id,))
    report = cursor.fetchone()
    conn.close()

    total_income, total_expense = report
    savings = total_income - total_expense

    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Savings: {savings}")
