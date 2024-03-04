"""Prototype of CLI assistant"""

from address_book import AddressBook
from assistant_functions import (
    add_birthday,
    add_contact,
    change_contact,
    get_all_contacts,
    get_contact_birthday,
    get_contact_phone,
    parse_input,
)
from errors import HELP_ERROR_MESSAGE

# TODO:
# show-birthday [ім'я]: Показати дату народження для вказаного контакту.
# birthdays: Показати дні народження, які відбудуться протягом наступного тижня.

# TODO: save and upload from file


def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "show-birthday":
            print(get_contact_birthday(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print(f"Unknown command '{command}', please try again.\n{HELP_ERROR_MESSAGE}")


if __name__ == "__main__":
    main()
