from person import Person
from typing import List

class Patient(Person):
    def __init__(self, name: str, contact_info: str, medical_history: List[str] = []):
        super().__init__(name, contact_info)
        self.medical_history = medical_history

    def view_medical_history(self) -> List[str]:
        return self.medical_history
