import copy
from patients import Patients

class Doctur:
    def __init__(self, name: str, contact_iformation: str):
        self._name = name
        self._contact_information = contact_iformation
        self._patients = []

    def add_patients(self, patient):
        self._patients.append(patient)

    def done_operat(self, patient):
        for i in range(len(self._patients)):
            if self._patients[i] == patient:
                del self._patients[i]

    @property
    def patients(self):
        return copy.deepcopy(self._patients)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def contact_iformation(self):
        return self._contact_information

    @contact_iformation.setter
    def contact_iformation(self, new_contact_information):
        self._contact_information = new_contact_information

def main():
    d = Doctur("Poxos", "hhhh")
    print(d.name)
    print(d.contact_iformation)
    d.name = "new name"
    d.contact_iformation = "new info"
    print(d.name)
    print(d.contact_iformation)

if __name__ == "__main__":
    main()

