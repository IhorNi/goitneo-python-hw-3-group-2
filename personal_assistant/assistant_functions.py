"""CLI assistant functions"""

from typing import Optional

from errors import AddInputError, ChangeInputError, PhoneInputError, input_error

Contacts = dict[str, str]
CommandArguments = list[str]


def parse_input(user_input: str) -> tuple[str, Optional[CommandArguments]]:
    if not user_input.strip():
        return "", None

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    if len(args) == 0:
        return cmd, None

    return cmd, *args


@input_error
def add_contact(args: CommandArguments, contacts: Contacts) -> str:
    if args is None or len(args) < 2:
        raise AddInputError()

    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: CommandArguments, contacts: Contacts) -> str:
    if args is None or len(args) < 2:
        raise ChangeInputError()

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated."
    else:
        return f"No contact named {name} exists."


@input_error
def print_phone(args: CommandArguments, contacts: Contacts) -> str:
    if args[0] is None:
        raise PhoneInputError()

    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"No contact named {name} exists."


def print_all(contacts: Contacts) -> str:
    if not contacts:
        return "No contacts stored."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
