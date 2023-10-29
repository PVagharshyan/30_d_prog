from validate_decorators import validate_non_empty_string, validate_positive_number
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def add_transaction(self, transaction):
        pass

class BasicAccount(Account):
    @validate_non_empty_string("account_number")
    @validate_positive_number("balance")
    @validate_non_empty_string("account_type")
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions
