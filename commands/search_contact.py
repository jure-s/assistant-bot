from commands.utils import validate_field


def search_contact_interactive(contacts):

    query = validate_field("Enter the search query: ", required=True).lower()

    def match_contact(contact):
        if query in contact.name.lower():
            return True
        if query in contact.phone:
            return True
        if contact.email and query in contact.email.lower():
            return True
        if contact.address and query in contact.address.lower():
            return True
        if contact.birthday and query in contact.birthday.strftime("%d.%m.%Y"):
            return True

        for note in contact.notes:
            if query in note.content.lower():
                return True
            if any(query in tag.lower() for tag in note.tags):
                return True
        return False

    results = [str(contact)
               for contact in contacts.values() if match_contact(contact)]

    if not results:
        return "No contacts found."
    return "\n".join(results)
