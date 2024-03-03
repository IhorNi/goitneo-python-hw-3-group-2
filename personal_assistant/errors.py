HELP_ERROR_MESSAGE = """Supported functions:
- 'add': Add new contact, the correct format is 'add username phone'
- 'change': Change existing contact, the correct format is 'change username phone'
- 'phone': Print existing contact number, the correct format is 'phone username'
- 'add-birthday': command expects two arguments 'name' and 'birthday'
- 'all': Print all existing contact numbers if any, the correct format is 'all'
- 'exit' | 'close': Close the app, the correct format 'exit' and 'close'
"""


class InputError(Exception):
    """Base class for other input exceptions"""

    pass


class AddContactInputError(InputError):
    def __str__(self):
        return "AddContactInputError: 'add' command expects two arguments 'name' and 'phone'."


class AddBirthdatInputError(InputError):
    def __str__(self):
        return "AddBirthdatInputError: 'add-birthday' command expects two arguments 'name' and 'birthday'."


class ChangeInputError(InputError):
    def __str__(self):
        return "ChangeInputError: 'change' command expects two arguments 'name' and 'phone'."


class PhoneInputError(InputError):
    def __str__(self):
        return "PhoneInputError: 'phone' command expects one argument 'name'."


class InaccurateBirthdayFormat(InputError):
    def __str__(self):
        return "Birthday must be in format DD.MM.YYYY."


class InaccuratePhoneFormat(InputError):
    def __str__(self):
        return "Phone number must contain exactly 10 digits."


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InputError as e:
            return str(e)

    return inner
