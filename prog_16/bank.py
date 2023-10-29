from abc import ABC, abstractmethod
from typing import List
from accounts import Account
from transactions import Transaction
from customers import Customer
import utility

class BankSystem(ABC):
    @abstractmethod
    def manage_account(self, customer: 'Customer', account: 'Account'):
        pass

    @abstractmethod
    def view_transaction_history(self, customer: 'Customer', account: 'Account') -> List['Transaction']:
        pass

    @abstractmethod
    def transfer_funds(self, sender_account: 'Account', recipient_account: 'Account', amount: float) -> 'Transaction':
        pass

class Bank(BankSystem):
    def __init__(self):
        self._customers = []

    @utility.type_checking(Customer, Account)
    def manage_account(self, customer: Customer, account: Account):
        customer.add_account(account)

    @utility.type_checking(Customer, Account)
    def view_transaction_history(self, customer: Customer, account: Account) -> List[Transaction]:
        if account in customer.accounts:
            return account.transactions
        else:
            raise ValueError("Account not found for this customer")

    @utility.type_checking(Account, Account, (float, int))
    def transfer_funds(self, sender_account: Account, recipient_account: Account, amount: float) -> Transaction:
        if amount <= 0:
            raise ValueError("Invalid amount for funds transfer")

        if sender_account.balance >= amount:
            sender_account.balance -= amount
            recipient_account.balance += amount
            sender_transaction = Transaction(sender_account, -amount, "Withdrawal")
            recipient_transaction = Transaction(recipient_account, amount, "Deposit")
            sender_account.transactions.append(sender_transaction)
            recipient_account.transactions.append(recipient_transaction)
            return sender_transaction
        else:
            raise ValueError("Insufficient balance for funds transfer")

    @property
    def customers(self):
        return self._customers

