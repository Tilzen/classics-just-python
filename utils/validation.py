from functools import wraps

def validate_type(type):
    def validate(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if all(isinstance(arg, type) for arg in args):
                return func(*args)
        return inner
    return validate
