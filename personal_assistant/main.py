"""Prototype of CLI assistant"""

from address_book import AddressBook
from assistant_functions import add_contact, change_contact, parse_input, print_all, print_phone
from errors import HELP_ERROR_MESSAGE

# TODO:
# add [ім'я] [телефон]: Додати новий контакт з іменем та телефонним номером.
# change [ім'я] [новий телефон]: Змінити телефонний номер для вказаного контакту.
# phone [ім'я]: Показати телефонний номер для вказаного контакту.
# all: Показати всі контакти в адресній книзі.

# add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
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
