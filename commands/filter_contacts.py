from datetime import datetime, timedelta

def filter_contacts_by_tag(contacts, tag):
    """
    Фільтрує контакти за тегами нотаток.
    """
    filtered_contacts = [
        contact for contact in contacts.values()
        if any(tag in note.tags for note in contact.notes)
    ]
    if not filtered_contacts:
        return f"No contacts found with tag '{tag}'."
    return "\n".join(str(contact) for contact in filtered_contacts)

def filter_contacts_by_birthday_range(contacts, days):
    """
    Фільтрує контакти за днями народження у заданому інтервалі.
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=days)
    filtered_contacts = []

    for contact in contacts.values():
        print(f"DEBUG: Processing contact: {contact.name}, Birthday: {contact.birthday}")
        if contact.birthday:
            try:
                if isinstance(contact.birthday, str):
                    contact_birthday = datetime.strptime(contact.birthday, "%d.%m.%Y").date()
                else:
                    contact_birthday = contact.birthday

                birthday_this_year = contact_birthday.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = contact_birthday.replace(year=today.year + 1)

                if today <= birthday_this_year <= end_date:
                    print(f"DEBUG: Contact {contact.name} has a birthday in range")
                    filtered_contacts.append(contact)
            except Exception as e:
                print(f"DEBUG: Error processing {contact.name}'s birthday: {e}")

    if not filtered_contacts:
        return f"No contacts with birthdays in the next {days} days."
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
        return f"No contacts found matching '{query}'."
    return "\n".join(str(contact) for contact in filtered_contacts)
