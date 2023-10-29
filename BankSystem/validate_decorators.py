from functools import wraps
import re

def validate_non_empty_string(field_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[1]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} cannot be empty or non-string type")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_positive_number(field_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[2]
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(f"{field_name} must be a positive number or zero")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_email(field_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[2]
            if not isinstance(value, str):
                raise ValueError(f"{field_name} must be a string")
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, value):
                raise ValueError(f"Invalid email address for {field_name}")

            return func(*args, **kwargs)
        return wrapper
    return decorator
