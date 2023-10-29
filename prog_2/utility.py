from email_validator import validate_email, EmailNotValidError
from cars import Car

class AddressNotValidError(Exception):
    pass

class PhoneNumberNotValidError(Exception):
    pass

class NameNotValidError(Exception):
    pass

class CommissionRateNotValidError(Exception):
    pass

class MakeNotValidError(Exception):
    pass

class ModelNotValidError(Exception):
    pass

class PriceNotValidError(Exception):
    pass

class CarsArrNotValidError(Exception):
    pass

class Utility:
    @staticmethod
    def check_address(address: str) -> bool:
        if not isinstance(address, str):
            raise AddressNotValidError("...")
        return True

    @staticmethod
    def check_email(email: str) -> bool:
        try:
            valid = validate_email(email)
        except EmailNotValidError as err:
            raise EmailNotValidError(err)
        return True

    @staticmethod
    def check_phone_number(phone_number: str) -> bool:
        if phone_number[0] != '0' or len(phone_number) != 9:
            raise PhoneNumberNotValidError("...")
        for i in range(len(phone_number)):
            if not phone_number[i].isnumeric():
                raise PhoneNumberNotValidError("...")
        return True

    @staticmethod
    def check_name(name: str) -> bool:
        if not isinstance(name, str):
            raise NameNotValidError("...")

    @staticmethod
    def check_commission_rate(commission_rate: float) -> bool:
        if not isinstance(commission_rate, (float, int)):
            raise CommissionRateNotValidError("...")
        return True

    @staticmethod
    def check_cars(cars: list["Cars"]) -> bool:
        if not isinstance(cars, list): raise CarsArrNotValidError("...")
        for i in range(len(cars)):
            if not isinstance(cars[i], Car):
                raise CarsArrNotValidError("...")
        return True
