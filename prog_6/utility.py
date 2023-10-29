class Utility:
    @staticmethod
    def check_age(age):
        if age > 1 and age < 100:
            return True
        return False

    @staticmethod
    def check_name(name):
        return isinstance(name, str)

    @staticmethod
    def check_medical_history(medical_history):
        return isinstance(medical_history, str)
