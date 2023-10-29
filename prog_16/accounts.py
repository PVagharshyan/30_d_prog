from transactions import Transaction, Account as Account_t
from typing import List
import utility

class Account(Account_t):
    def __init__(self, account_number: str, balance: float, account_type: str):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transactions = []

    @property
    def account_number(self) -> str:
        return self._account_number

    @account_number.setter
    @utility.type_checking(str)
    def account_number(self, value: str):
        self._account_number = value

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    @utility.type_checking((float, int))
    def balance(self, value: float):
        self._balance = float(value)

    @property
    def account_type(self) -> str:
        return self._account_type

    @account_type.setter
    @utility.type_checking(str)
    def account_type(self, value: str):
        self._account_type = value

    @property
    def transactions(self) -> List['Transaction']:
        return self._transactions

    @transactions.setter
    @utility.container_type_checking(list, Transaction)
    def transactions(self, value: List['Transaction']):
        self._transactions = value

class IndividualAccount(Account):
    def __init__(self, account_number: str, balance: float, account_type: str):
        super().__init__(account_number, balance, account_type)

class JointAccount(Account):
    def __init__(self, account_number: str, balance: float, account_type: str):
        super().__init__(account_number, balance, account_type)
