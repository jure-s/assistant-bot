from commands.utils import validate_field

def search_notes_interactive(contacts):
    """
    Інтерактивний пошук нотаток у контакті.
    """
    name = validate_field("Enter the name of the contact to search notes for: ", required=True)
    contact = contacts.get(name)
    if not contact:
        return f"Contact {name} not found."

    query = validate_field("Enter the search query: ", required=True).lower()
    results = contact.search_notes(query)
    return "\n".join(str(note) for note in results) if results else "No notes found."