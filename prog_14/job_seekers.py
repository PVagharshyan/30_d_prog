from info import Info
import utility

class JobSeeker:
    def __init__(self, name: str, contact_info: str, resume: str):
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value

    @property
    def resume(self) -> str:
        return self._resume

    @resume.setter
    @utility.type_checking(str)
    def resume(self, value: str):
        self._resume = value
