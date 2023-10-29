from accounts import Account
from typing import List
import utility

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self._accounts = []

    @utility.type_checking(Account)
    def add_account(self, account: 'Account'):
        self._accounts.append(account)

    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    @utility.container_type_checking(list, Account)
    def accounts(self, value: List[Account]):
        self._accounts = value

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value
