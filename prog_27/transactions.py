from accounts import Account
from abc import ABC, abstractmethod
from typing import List
import utility

class Transaction:
    def __init__(self, account: Account, transaction_type: str, amount: float):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    @property
    def account(self) -> Account:
        return self._account

    @account.setter
    @utility.type_checking(Account)
    def account(self, new_account: Account):
        self._account = new_account

    @property
    def transaction_type(self) -> str:
        return self._transaction_type

    @transaction_type.setter
    @utility.type_checking(str)
    def transaction_type(self, new_transaction_type: str):
        self._transaction_type = new_transaction_type

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    @utility.type_checking((int, float))
    def amount(self, new_amount: float):
        self._amount = new_amount
