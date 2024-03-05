## Examples to test cli assistant
```
add // expected error AddContactInputError
add Jake // expected error AddContactInputError
add Jake 1237456 // expected error InaccuratePhoneFormat
add Jake 1234567890
add-birthday // expected error AddBirthdatInputError
add-birthday Jake 1996-12-26  // expected error InaccurateBirthdayFormat
add-birthday Jake 06.03.1998
add-birthday Jane 06.03.1998 // expected error NonExistingContact
add Jane 0987654321
add-birthday Jane 08.03.1998
all // prints 2 contacts
exit // exit to test saving to a file
all // prints 2 contacts
change // expected error ChangeInputError
change Jak // expected error ChangeInputError
change Jak 1237456 // expected error NonExistingContact
change Jake 1237456 // expected error InaccuratePhoneFormat
change Jake 6574839210
phone // expected error PhoneInputError
phone Jak // expected error NonExistingContact
phone Jake
show-birthday // expected error GetBirthdayInputError
show-birthday Jak // expected error NonExistingContact
show-birthday Jake
add Jason 8764329119
add-birthday Jason 04.03.1989
add Jakob 8764329119
add-birthday Jakob 09.03.1994
add Julia 1234329119
add-birthday Julia 25.03.1921
birthdays  // output depends on a date of testing
```