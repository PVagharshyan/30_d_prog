from functools import wraps

def type_checking(*type_name):
    def check_inner(func):
        @wraps(func)
        def inner(self, *value) -> None:
            if len(type_name) != len(value):
                raise Exception("...")
            for i in range(len(type_name)):
                if not isinstance(value[i], type_name[i]):
                    raise ValueError("...")
            return func(self, *value)
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
