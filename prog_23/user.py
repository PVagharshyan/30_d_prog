import utility

class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name):
        self._name = new_name

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, new_contact_info):
        self._contact_info = new_contact_info
