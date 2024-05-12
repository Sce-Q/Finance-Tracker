# 1. Introduction
## What is your application?:
* The application is a personal finance tracker called "FinanceTracker" that allows users to manage their expenses. It is a command-line interface (CLI) program written in Python.
## How to run the program?:
* To run the program, simply execute the Python script.
## How to use the program?:
* The program provides a menu-driven interface that allows users to add themselves to the system, record their expenses, remove expenses, view their expense history, or exit the program.

# 2. Body/Analysis
The program implements the following functional requirements:
## User Management: 
* The program allows users to add themselves to the system using the add_user method. This method checks if the user already exists in the system and adds them if they don't. 
* ![image](https://github.com/Sce-Q/Finance-Tracker/assets/157913107/ef6a8298-4f39-4e76-96fc-f8aec1d4fbe0)

## Expense Management:
* The program allows users to add expenses using the add_expense method. This method checks if the user exists in the system and adds the expense to their record.
* ![image](https://github.com/Sce-Q/Finance-Tracker/assets/157913107/716dd4a2-90f9-461c-b747-8ca15a092c7c)

## Expense Removal: 
* The program allows users to remove expenses using the remove_expense method. This method checks if the user exists in the system and removes the expense from their record.
* ![image](https://github.com/Sce-Q/Finance-Tracker/assets/157913107/c2664e8a-adfc-4e4d-a974-f67803c15aa0)

## Expense History:
* The program allows users to view their expense history using the print_expense_history method. This method checks if the user exists in the system and prints their expense history.
* ![image](https://github.com/Sce-Q/Finance-Tracker/assets/157913107/82bccec9-ed2c-4cda-be97-980cb699cc78)

## Data Storage:
* The program stores the data in a JSON file using the load_expense_history and save_expense_history methods. These methods load and save the data to the file, respectively.
* ![image](https://github.com/Sce-Q/Finance-Tracker/assets/157913107/eaeff7bf-d40f-4aec-897c-9bb0dca76673)


# 3. Results and Summary
Results: The program successfully implements the required features for a personal finance tracker. The program's data storage mechanism allows for persistent data storage between program runs. The program's CLI interface is easy to use and intuitive.
Conclusions: In conclusion, this coursework has achieved a functional personal finance tracker application that meets the defined objectives and functional requirements. The program provides a simple and intuitive interface for users to manage their expenses.
Future Extensions: It would be possible to extend the application by adding more features, such as budgeting and expense categorization, and improving the user interface. Additionally, the program could be modified to support multiple users and provide more advanced data analysis and visualization capabilities.
