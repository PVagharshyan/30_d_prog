import utility
from info import Info

class Student:
    def __init__(self, name: str, contact_information: Info) -> None:
        self.name = name
        self.contact_information = contact_information

    def __str__(self) -> str:
        return f"name: {self.name},\ncontact information:\n {self.contact_information}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.check_str_data
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def contact_information(self) -> str:
        return self._contact_information.__str__()

    @contact_information.setter
    def contact_information(self, new_contact_information: Info) -> None:
        self._contact_information = new_contact_information


def main():
    i = Info("085258585", "dafdas", "paylak.vagharshyan@gmail.com")
    s = Student("sdsds", i)
    print(s)

if __name__ == "__main__":
    main()
