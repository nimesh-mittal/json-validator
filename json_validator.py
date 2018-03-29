from jsonschema import Draft4Validator
from functools import wraps


def validate_schema(json_obj, schema):
    validator = Draft4Validator(schema)

    def wrapper(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            input = json_obj
            errors = [error.message for error in validator.iter_errors(input)]
            if errors:
                return dict(error=dict(code="ERRROR", message=errors), data=False)
            else:
                return fn(*args, **kwargs)
        return wrapped
    return wrapper


def validate_v1(json_obj, schema):
    validator = Draft4Validator(schema)
    return [error.message for error in validator.iter_errors(json_obj)]