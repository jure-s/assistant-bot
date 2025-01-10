def sort_contacts(contacts, field):
    def contact_key(contact):
        value = getattr(contact, field, "")
        if isinstance(value, str):
            return value.lower()
        return value or ""

    sorted_contacts = sorted(contacts.values(), key=contact_key)
    return sorted_contacts