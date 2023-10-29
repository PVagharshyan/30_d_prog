from functools import wraps

def type_checking(type_name):
    def check_inner(func):
        @wraps(func)
        def inner(self, value: type_name) -> None:
            if not isinstance(value, type_name):
                raise ValueError("...")
            return func(self, value)
        return inner
    return check_inner

def container_type_checking(container_type, type_name):
    def check_inner(func):
        @wraps(func)
        def inner(self, value: container_type[f'type_name']) -> None:
            if not isinstance(value, container_type):
                raise ValueError("Not valis container")
            for i in value:
                if not isinstance(i, type_name):
                    raise ValueError("Not valid elements!")
            return func(self, value)
        return inner
    return check_inner

def display_array(array) -> str:
    result = ""
    for i in array:
        result += str(i) + "\n"
    return result


