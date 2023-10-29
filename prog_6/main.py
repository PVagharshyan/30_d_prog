from medicalStaff import Driver, Nurse
from doctors import Doctur
from patients import Patients

def main():
    doctur = Doctur("Poxos", "very good doctor")
    patient_1 = Patients("Patient_1", 20, "10 were operated on")
    patient_2 = Patients("Patient_2", 21, "15 were operated on")
    doctur.add_patients(patient_1)
    doctur.add_patients(patient_2)
    patients = doctur.patients
    for i in patients:
        print(i)


if __name__ == "__main__":
    main()
