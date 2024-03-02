HELP_ERROR_MESSAGE = """Supported functions:
- 'add': Add new contact, the correct format is 'add username phone'
- 'change': Change existing contact, the correct format is 'change username phone'
- 'phone': Print existing contact number, the correct format is 'phone username'
- 'all': Print all existing contact numbers if any, the correct format is 'all'
- 'exit' | 'close': Close the app, the correct format 'exit' and 'close'
"""


class InputError(Exception):
    """Base class for other input exceptions"""

    pass


class AddInputError(InputError):
    def __str__(self):
        return "AddInputError: 'add' command expects two arguments 'name' and 'phone'."


class ChangeInputError(InputError):
    def __str__(self):
        return "ChangeInputError: 'change' command expects two arguments 'name' and 'phone'."


class PhoneInputError(InputError):
    def __str__(self):
        return "PhoneInputError: 'phone' command expects one argument 'name'."


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InputError as e:
            return str(e)

    return inner
