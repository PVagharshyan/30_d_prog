from customers import Customer
from accounts import Account
from abc import ABC, abstractmethod
from typing import List
import utility

class Bank(ABC):
    @abstractmethod
    def manage_account(self, customer: Customer, account: Account):
        pass

    @abstractmethod
    def view_transaction_history(self, account: Account):
        pass

    @abstractmethod
    def transfer_funds(self, from_account: Account, to_account: Account, amount: float):
        pass

class BankSystem(Bank):
    @utility.type_checking(Customer, Account)
    def manage_account(self, customer: Customer, account: Account):
        customer.accounts.append(account)

    @utility.type_checking(Account)
    def view_transaction_history(self, account: Account):
        pass

    @utility.type_checking(Account, Account, (int, float))
    def transfer_funds(self, from_account: Account, to_account: Account, amount: float):
        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            transaction1 = Transaction(from_account, "Withdrawal", amount)
            transaction2 = Transaction(to_account, "Deposit", amount)
        else:
            print("Insufficient funds for the transfer.")
