

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Expense:
    #Represents an individual financial expense.
    
    def __init__(self, title: str, amount: float):
        #Initialize a new expense with title and amount.
        # Input validation
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number")
            
        self.id = str(uuid.uuid4())
        self.title = title.strip()
        self.amount = float(amount)
        self.created_at = datetime.now(datetime.timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: Optional[str] = None, amount: Optional[float] = None) -> None:
        #Update expense title and/or amount, updating timestamp if changes occur.
        changes_made = False
        
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("Title must be a non-empty string")
            self.title = title.strip()
            changes_made = True
            
        if amount is not None:
            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError("Amount must be a non-negative number")
            self.amount = float(amount)
            changes_made = True
            
        if changes_made:
            self.updated_at = datetime.now(datetime.timezone.utc)

    def to_dict(self) -> Dict:
        #Return expense data as a dictionary.
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class ExpenseDatabase:
    #Manages a collection of Expense objects.
    
    def __init__(self):
        #Initialize an empty expense database.
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        #Add an expense to the database.
        if not isinstance(expense, Expense):
            raise ValueError("Can only add Expense objects")
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str) -> bool:
        #Remove an expense by ID and return True if successful.
        initial_length = len(self.expenses)
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
        return len(self.expenses) < initial_length

    def get_expense_by_id(self, expense_id: str) -> Optional[Expense]:
        #Retrieve an expense by its ID.
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title: str) -> List[Expense]:
        #Retrieve all expenses matching the given title (case-insensitive).
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        return [exp for exp in self.expenses if exp.title.lower() == title.lower()]

    def to_dict(self) -> List[Dict]:
    #Return all expenses as a list of dictionaries.
        return [expense.to_dict() for expense in self.expenses]

