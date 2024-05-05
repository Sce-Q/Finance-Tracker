import datetime
import json
import os

class FinanceTracker:
    def __init__(self, filepath):
        self.filepath = filepath
        self.users = self.load_expense_history()

    def load_expense_history(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as file:
                    data = json.load(file)
                    if isinstance(data, dict) and 'users' in data:
                        return data['users']
                    else:
                        return {}
            except json.JSONDecodeError:
                return {}
        else:
            return {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = {'expenses': []}
            print(f"User {username} added")
        else:
            print(f"User {username} already exists")

    def add_expense(self, amount, description, user):
        if user in self.users:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            expense = {
                'Amount': amount,
                'Description': description,
                'Purchase time': timestamp
            }
            self.users[user]['expenses'].append(expense)
            print(f"Added expense for {user}: {description} for {amount:.2f}€")
            self.save_expense_history()
        else:
            print(f"User {user} does not exist")

    def remove_expense(self, index, user):
        if user in self.users:
            if 0 <= index < len(self.users[user]['expenses']):
                removed = self.users[user]['expenses'].pop(index)
                print(f"Removed expense for {user}: {removed['Description']} for {removed['Amount']:.2f}€")
                self.save_expense_history()
            else:
                print("Invalid index")
        else:
            print(f"User {user} does not exist")

    def print_expense_history(self, user):
        if user in self.users:
            if not self.users[user]['expenses']:
                print(f"No expenses recorded for {user}.")
                return
            for i, expense in enumerate(self.users[user]['expenses'], 1):
                print(f"{i}. {expense['Purchase time']}: {expense['Description']} - {expense['Amount']:.2f}€")
        else:
            print(f"User {user} does not exist")

    def save_expense_history(self):
        data = {'users': self.users}
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Expense history saved to {self.filepath}")

def main():
    filepath = "expenses.json"
    tracker = FinanceTracker(filepath)

    while True:
        print("\n1. Add user")
        print("2. Add expense")
        print("3. Remove expense")
        print("4. Print expense history")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            tracker.add_user(username)
        elif choice == "2":
            username = input("Enter username: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            tracker.add_expense(amount, description, username)
        elif choice == "3":
            username = input("Enter username: ")
            index = int(input("Enter expense index: ")) - 1
            tracker.remove_expense(index, username)
        elif choice == "4":
            username = input("Enter username: ")
            tracker.print_expense_history(username)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()