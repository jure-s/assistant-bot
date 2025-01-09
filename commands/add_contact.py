from models.contact import Contact
from models.validation import validate_phone, validate_email
from datetime import datetime


def add_contact_interactive(contacts):
    """
    Інтерактивне додавання контакту.
    """
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email (optional): ").strip()
    birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    address = input("Enter address (optional): ").strip()

    if name in contacts:
        return f"Contact {name} already exists."

    try:
        phone = validate_phone(phone)
        email = validate_email(email) if email else None
        birthday = datetime.strptime(
            birthday, "%d.%m.%Y").date() if birthday else None
    except ValueError as e:
        return f"Error: {e}"

    contact = Contact(name, phone, email, birthday, address)
    contacts[name] = contact
    return f"Contact {name} added successfully."
