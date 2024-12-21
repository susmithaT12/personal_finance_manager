from transactions import add_transaction, view_transactions, generate_report, set_budget, view_budget
import hashlib

# In-memory user storage (to be replaced with database integration)
users = {}
user_id_counter = 1  # Simulate user IDs for simplicity

# Hash password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User registration function
def register_user():
    global user_id_counter
    print("Register a new account.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    hashed_password = hash_password(password)

    # Check if the username is unique
    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    # Save user details
    users[username] = {'password': hashed_password, 'user_id': user_id_counter}
    user_id_counter += 1
    print("Registration successful!")

# User login function
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    # Validate username and password
    if username in users and users[username]['password'] == hashed_password:
        print(f"Login successful! Welcome, {username}.")
        user_id = users[username]['user_id']
        user_menu(user_id)
    else:
        print("Login failed. Invalid credentials.")

# User menu function
def user_menu(user_id):
    while True:
        print("\nMain Menu")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Set Budget")
        print("5. View Budget")
        print("6. Logout")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Collect transaction details from the user
                amount = float(input("Enter the transaction amount: "))
                category = input("Enter the transaction category: ")
                transaction_type = input("Enter the transaction type (Income/Expense): ")
                description = input("Enter a description for the transaction: ")
                add_transaction(user_id, amount, category, transaction_type, description)

            elif choice == 2:
                view_transactions(user_id)

            elif choice == 3:
                generate_report(user_id)

            elif choice == 4:
                budget_amount = float(input("Enter the budget amount: "))
                set_budget(user_id, budget_amount)


            elif choice == 5:
                view_budget(user_id)

            elif choice == 6:
                print("You have logged out successfully.")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Main menu function
def main_menu():
    while True:
        print("Welcome to the Personal Finance Management App!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                register_user()
            elif choice == 2:
                login_user()
            elif choice == 3:
                print("Exiting the app.")
                exit()
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Starting point of the app
if __name__ == "__main__":
    main_menu()
