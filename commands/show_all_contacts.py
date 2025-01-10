def show_all_contacts(contacts):
    if not contacts:
        return "The contact book is empty."
    return "\n".join(str(contact) for contact in contacts.values())
