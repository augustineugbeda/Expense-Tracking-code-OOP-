# Expense-Tracking-code-OOP-


## Project Description

Expense-Tracking-code-OOP is a Python-based application that demonstrates object-oriented programming (OOP) concepts through the implementation of two main classes: `Expense` and `ExpenseDatabase`. This project allows users to:
- Create and manage individual financial expenses
- Store and organize multiple expenses in a database
- Perform basic operations like adding, updating, removing, and querying expenses

The project showcases fundamental OOP principles including encapsulation, abstraction, and single responsibility while providing a practical example of financial expense management.

### Features
- Unique expense identification using UUID
- Timestamp tracking for creation and updates (UTC)
- Input validation for data integrity
- Flexible expense updating
- Case-insensitive title searching
- Dictionary-based data export

### Classes
1. **Expense**
   - Represents individual financial transactions
   - Attributes: id, title, amount, created_at, updated_at
   - Methods: update(), to_dict()

2. **ExpenseDatabase**
   - Manages a collection of Expense objects
   - Attributes: expenses (list)
   - Methods: add_expense(), remove_expense(), get_expense_by_id(), get_expense_by_title(), to_dict()

## Prerequisites
- Python 3.7+
- No external dependencies required

## How to Clone the Repository

Follow these steps to get a copy of the project on your local machine:

1. **Using Git**
```bash
# Clone the repository
git clone https://github.com/augustineugbeda/Expense-Tracking-code-OOP.git

# Navigate to the project directory
cd Expense-Tracking-code-OOP

```


2. Manual Download
   - Visit the repository URL
   - Click "Code" > "Download ZIP"
   - Extract the ZIP file to your desired location
   - Navigate to the extracted folder

### How to Run the Code
## Basic Execution
Ensure Python is installed on your system:
```bash
python --version
```
## Run the script directly:
```bash
python Expense_ExpenseDatabase.py
```
