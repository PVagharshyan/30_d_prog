from email_validator import validate_email, EmailNotValidError
from functools import wraps

#student

class DataStrNotValidError(Exception):
    pass

class PhoneNumberNotValidError(Exception):
    pass

def check_email(func):
    @wraps(func)
    def inner(self, email: str):
        validate_email(email)
        return func(self, email)
    return inner

def check_str_data(func):
    @wraps(func)
    def inner(self, data: str):
        if not isinstance(data, str):
            raise DataStrNotValidError("...")
        return func(self, data)
    return inner

def check_phone_number(func):
    @wraps(func)
    def inner(self, phone_number: int):
        if phone_number[0] != '0' or len(phone_number) != 9:
            raise PhoneNumberNotValidError("...")
        for i in range(len(phone_number)):
            if not phone_number[i].isnumeric():
                raise PhoneNumberNotValidError("...")
        return func(self, phone_number)
    return inner
#////////

