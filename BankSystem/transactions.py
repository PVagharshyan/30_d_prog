from abc import ABC, abstractmethod

# Interfaces
class Transaction(ABC):
    @abstractmethod
    def execute(self):
        ...

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        ...

    @abstractmethod
    def withdraw(self, amount):
        ...

    @abstractmethod
    def add_transaction(self, transaction):
        ...

# Concrete Classes
class DepositTransaction(Transaction):
    def __init__(self, account, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0 for a deposit transaction.")
        self.account = account
        self.amount = amount
        self.transaction_type = "Deposit"

    def execute(self):
        self.account.deposit(self.amount)
        self.account.add_transaction(self)

class WithdrawTransaction(Transaction):
    def __init__(self, account, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0 for a withdrawal transaction.")
        self.account = account
        self.amount = amount
        self.transaction_type = "Withdrawal"

    def execute(self):
        if self.account.balance < self.amount:
            raise ValueError("Insufficient funds")
        self.account.withdraw(self.amount)
        self.account.add_transaction(self)

class TransferTransaction(Transaction):
    def __init__(self, from_account, to_account, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0 for a transfer transaction.")
        if from_account == to_account:
            raise ValueError("From and To accounts must be different for a transfer transaction.")
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = "Transfer"

    def execute(self):
        if self.from_account.balance < self.amount:
            raise ValueError("Insufficient funds")
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        self.from_account.add_transaction(self)
        self.to_account.add_transaction(self)


