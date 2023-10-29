from email_validator import validate_email, EmailNotValidError
from functools import wraps
from typing import List, Dict

class DataStrNotValidError(Exception):
    pass

class PhoneNumberNotValidError(Exception):
    pass

class DishesNotValidError(Exception):
    pass

class PricesNotValidError(Exception):
    pass

class NumericNotValidError(Exception):
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

def check_num_data(func):
    @wraps(func)
    def inner(self, num: (float, int)):
        if not isinstance(num, (float, int)):
            raise NumericNotValidError("...")
        return func(self, num)
    return inner

def check_order_items(func):
    @wraps(func)
    def inner(self, order_items):
        if not isinstance(order_items, list):
            raise OrderItemsNotValidError("...")
        for i in order_items:
            if not isinstance(i, str):
                raise OrderItemsNotValidError("...")
        return func(self, order_items)
    return inner
