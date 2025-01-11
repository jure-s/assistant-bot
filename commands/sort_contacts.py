def sort_contacts(contacts, field):
    """
    Сортує контакти за заданим полем.
    """
    def contact_key(contact):
        value = getattr(contact, field, "")
        if isinstance(value, str):
            return value.lower()
        return value or ""

    return sorted(contacts.values(), key=contact_key)
