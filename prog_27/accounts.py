from abc import ABC, abstractmethod
from typing import List
import utility

class Account:
    def __init__(self, account_number: str, account_type: str):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0

    @property
    def account_number(self) -> str:
        return self._account_number

    @account_number.setter
    @utility.type_checking(str)
    def account_number(self, new_account_number: str):
        self._account_number = new_account_number

    @property
    def account_type(self) -> str:
        return self._account_type

    @account_type.setter
    @utility.type_checking(str)
    def account_type(self, new_account_type: str):
        self._account_type = new_account_type

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    @utility.type_checking((int, float))
    def balance(self, new_balance: float):
        if new_balance >= 0.0:
            self._balance = new_balance
        else:
            raise ValueError("Balance must be non-negative")

class IndividualAccount(Account):
    def __init__(self, account_number: str):
        super().__init__(account_number, "Individual")

class BusinessAccount(Account):
    def __init__(self, account_number: str):
        super().__init__(account_number, "Business")
