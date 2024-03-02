"""Prototype of CLI assistant"""

from assistant_functions import add_contact, change_contact, parse_input, print_all, print_phone
from errors import HELP_ERROR_MESSAGE


def main():
    contacts = {}
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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_phone(args, contacts))
        elif command == "all":
            print(print_all(contacts))
        else:
            print(f"Unknown command '{command}', please try again.\n{HELP_ERROR_MESSAGE}")


if __name__ == "__main__":
    main()
