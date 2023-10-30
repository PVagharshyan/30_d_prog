from typing import Optional
import utility

class Person:
    def __init__(self, name: str, contact_info: str):
        self.name: str = name
        self.contact_info: str = contact_info

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, new_contact_info: str) -> None:
        self._contact_info = new_contact_info
