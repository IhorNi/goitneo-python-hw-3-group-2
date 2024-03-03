"""CLI assistant functions"""

from typing import Optional

from address_book import AddressBook, Record
from errors import (
    AddContactInputError, ChangeInputError, PhoneInputError, AddBirthdatInputError, input_error
)

Contacts = dict[str, str]
CommandArguments = list[str]


def parse_input(user_input: str) -> tuple[str, Optional[CommandArguments]]:
    if not user_input.strip():
        return "", None

    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().lower()

    if len(args) == 0:
        return cmd, None

    return cmd, *args


@input_error
def add_contact(args: CommandArguments, contacts: AddressBook) -> str:
    if args is None or len(args) < 2:
        raise AddContactInputError()

    name, phone = args
    new_contact = Record(name)
    new_contact.add_phone(phone)
    contacts.add_record(new_contact)
    return f"Contact {name} added."


@input_error
def change_contact(args: CommandArguments, contacts: AddressBook) -> str:
    if args is None or len(args) < 2:
        raise ChangeInputError()

    name, phone = args
    contact = contacts.find(name)
    if not contact:
        return f"No contact named {name} exists."

    contact.edit_phone(contact.phones[0].value, phone)
    return f"Phone number for {name} updated."


@input_error
def print_phone(args: CommandArguments, contacts: AddressBook) -> str:
    if args[0] is None:
        raise PhoneInputError()

    name = args[0]
    contact = contacts.find(name)
    if not contact:
        return f"No contact named {name} exists."

    return str(contact)


@input_error
def add_birthday(args: CommandArguments, contacts: AddressBook) -> str:
    if args is None or len(args) < 2:
        raise AddBirthdatInputError()

    name, date = args
    contact = contacts.find(name)
    if not contact:
        return f"No contact named {name} exists."

    contact.add_birthday(date)
    return f"Birthday added for {name} updated."


def print_all(contacts: AddressBook) -> str:
    if not contacts:
        return "No contacts stored."
    else:
        return "\n".join([str(contact) for contact in contacts.data.values()])
