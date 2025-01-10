from models.contact import Contact
from models.validation import validate_phone, validate_email
from datetime import datetime
from colorama import Fore


def validate_field(prompt, validation_func=None, required=False):
    while True:
        value = input(Fore.YELLOW + prompt).strip()
        if not value and not required:
            return None
        if not validation_func:
            return value
        try:
            return validation_func(value)
        except ValueError as e:
            print(Fore.RED + f"Error: {e}. Please try again.")


def add_contact_interactive(contacts):
    name = validate_field("Enter name: ", required=True)
    phone = validate_field("Enter phone: ", validate_phone, required=True)
    email = validate_field("Enter email: ", validate_email)
    birthday = validate_field(
        "Enter birthday (DD.MM.YYYY): ",
        lambda x: datetime.strptime(x, "%d.%m.%Y").date()
    )
    address = input(Fore.YELLOW + "Enter address: ").strip()

    note_content = input(
        Fore.YELLOW + "Add a note for this contact (or leave blank): ").strip()
    note_tags = (
        input(Fore.YELLOW +
              "Enter tags for the note (comma-separated): ").strip().split(",")
        if note_content
        else []
    )

    if name in contacts:
        return Fore.RED + f"Contact {name} already exists."

    contact = Contact(name, phone, email, birthday, address)
    if note_content:
        contact.add_note(note_content, note_tags)

    contacts[name] = contact
    return Fore.GREEN + f"Contact {name} added successfully."
