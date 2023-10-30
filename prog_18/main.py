from appointments import Appointment
from appointment_type import InPersonAppointment, VirtualAppointment
from doctors import Doctor
from health_care_system import HealthCareSystem
from patients import Patient

if __name__ == "__main__":
    healthcare_system = HealthCareSystem()

    patient1 = Patient("Alice", "alice@example.com", ["Fever"])
    doctor1 = Doctor("Dr. Smith", "drsmith@example.com", "Cardiologist")

    appointment1 = healthcare_system.schedule_appointment(patient1, doctor1, "2023-11-01 10:00 AM", InPersonAppointment())

    print(f"Appointment type: {appointment1.appointment_type.get_type()}")
    print(f"Patient's medical history: {healthcare_system.view_patient_medical_history(patient1)}")
