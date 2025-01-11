from datetime import datetime
from colorama import Fore

def filter_contacts_by_tag(contacts, tag):
    """
    Фільтрує контакти за тегами нотаток.
    """
    filtered_contacts = [
        contact for contact in contacts.values()
        if any(tag in note.tags for note in contact.notes)
    ]
    if not filtered_contacts:
        return Fore.YELLOW + f"No contacts found with tag '{tag}'."
    return "\n".join(str(contact) for contact in filtered_contacts)

def filter_contacts_by_birthday_date(contacts, date_str):
    """
    Фільтрує контакти за конкретною датою дня народження.
    """
    try:
        target_date = datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError:
        return Fore.RED + "Invalid date format. Please use DD.MM.YYYY."

    filtered_contacts = [
        contact for contact in contacts.values()
        if contact.birthday and contact.birthday.day == target_date.day and contact.birthday.month == target_date.month
    ]

    if not filtered_contacts:
        return Fore.YELLOW + f"No contacts found with birthdays on {date_str}."
    return "\n".join(str(contact) for contact in filtered_contacts)

def filter_contacts_by_query(contacts, query):
    """
    Фільтрує контакти за частиною імені, email або телефону.
    """
    query = query.lower()
    filtered_contacts = [
        contact for contact in contacts.values()
        if query in contact.name.lower()
        or (contact.email and query in contact.email.lower())
        or query in contact.phone
    ]
    if not filtered_contacts:
        return Fore.YELLOW + f"No contacts found matching '{query}'."
    return "\n".join(str(contact) for contact in filtered_contacts)
