import json
import re
from collections import UserDict, defaultdict
from datetime import date, datetime
from typing import List, Optional

from errors import InaccurateBirthdayFormat, InaccuratePhoneFormat

ADDRESS_BOOK_FILENAME = "address_book.json"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Next Monday"]
MONDAY_INDEX = 0
NEXT_MONDAY_INDEX = -1


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        if not re.match(r"^\d{10}$", value):
            raise InaccuratePhoneFormat()
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", value):
            raise InaccurateBirthdayFormat()
        super().__init__(value)

    def get_birthday_datetime(self) -> date:
        return datetime.strptime(self.value, "%d.%m.%Y").date()


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_phone(self, phone: str) -> None:
        new_phone = Phone(phone)
        if new_phone:
            self.phones.append(new_phone)

    def delete_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for index, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[index] = Phone(new_phone)
                break

    def find_phone(self, phone: str) -> Optional[str]:
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def to_dict(self):
        return {
            "name": self.name.value,
            "phones": [phone.value for phone in self.phones],
            "birthday": self.birthday.value if self.birthday else None,
        }

    @classmethod
    def from_dict(cls, data: dict):
        record = cls(data["name"])
        for phone in data["phones"]:
            record.add_phone(phone)
        if data["birthday"]:
            record.add_birthday(data["birthday"])
        return record

    def __str__(self) -> str:
        return (
            f"Contact name: {self.name}, birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):
    def save_to_file(self, filename: str = ADDRESS_BOOK_FILENAME) -> None:
        with open(filename, "w") as f:
            records_list = [record.to_dict() for record in self.data.values()]
            json.dump(records_list, f)

    @staticmethod
    def load_from_file(filename: str = ADDRESS_BOOK_FILENAME) -> "AddressBook":
        with open(filename, "r") as f:
            records_list = json.load(f)
        address_book = AddressBook()
        for record_dict in records_list:
            record = Record.from_dict(record_dict)
            address_book.add_record(record)
        return address_book

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
            print(f"{name} record is deleted")
        else:
            print(f"No records found by the name {name}")

    def get_birthdays_per_week(self, relative_date: date = datetime.today().date()) -> str:
        """
        Determine which colleagues have birthdays in the upcoming week.

        Args:
            relative_date (date, optional): The date from which to calculate one week forward. Default is today's date.

        Returns:
            str: A formatted string containing the names of colleagues that have birthdays
                in the upcoming week, sorted by the day of the week.
        """
        next_week_birthday_colleagues = defaultdict(list)

        for colleague in self.data.values():
            name = colleague.name
            birthday = colleague.birthday.get_birthday_datetime()
            if not birthday:
                continue
            birthday_this_year = self._get_birthday_this_year(birthday, relative_date)

            delta_days = (birthday_this_year - relative_date).days
            if delta_days < 7:
                weekday_to_greet = self._get_greeting_day(birthday_this_year, relative_date)
                next_week_birthday_colleagues[weekday_to_greet].append(
                    f"{name} ({birthday_this_year.strftime('%Y-%m-%d')})"
                )

        relative_date_str = f"{relative_date.strftime('%Y-%m-%d')}, {WEEKDAYS[relative_date.weekday()]}"

        greeting_string = f"---\nColleagues to greet for the next week, as of {relative_date_str}:\n---"
        if next_week_birthday_colleagues:
            for day, names in next_week_birthday_colleagues.items():
                greeting_string += f"\n{day}: {', '.join(names)}"
        else:
            greeting_string += "\nNo birthdays this week :("

        return greeting_string

    @staticmethod
    def _get_birthday_this_year(birthday: date, relative_date: date) -> date:
        """
        Returns this year's birthday based on a given reference date.

        Args:
            birthday (date): The birthday date.
            relative_date (date): The reference date.

        Returns:
            date: This year's birthday based on the reference date.
        """

        birthday_this_year = birthday.replace(year=relative_date.year)
        if birthday_this_year < relative_date:
            birthday_this_year = birthday_this_year.replace(year=relative_date.year + 1)

        return birthday_this_year

    @staticmethod
    def _get_greeting_day(birthday_this_year: date, relative_date: date) -> str:
        """
        Returns the weekday to greet the colleague.

        Args:
            birthday_this_year (date): The colleague's birthday this year.
            relative_date (date): The reference date.

        Returns:
            str: The weekday to greet the colleague.
        """

        # if birthday is a weekend and relative_date is Monday, so greeting goes to next Monday
        if (birthday_this_year.weekday() >= 5) & (relative_date.weekday() == 0):
            return WEEKDAYS[NEXT_MONDAY_INDEX]
        elif birthday_this_year.weekday() >= 5:
            return WEEKDAYS[MONDAY_INDEX]
        else:
            return WEEKDAYS[birthday_this_year.weekday()]
