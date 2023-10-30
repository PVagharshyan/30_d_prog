from accounts import Account
from abc import ABC, abstractmethod
from typing import List
import utility

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.accounts: List[Account] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name: str):
        self._name = new_name

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, new_contact_info: str):
        self._contact_info = new_contact_info

    @property
    def accounts(self) -> List[Account]:
        return self._accounts

    @accounts.setter
    @utility.container_type_checking(list, Account)
    def accounts(self, new_accounts: List[Account]):
        self._accounts = new_accounts
