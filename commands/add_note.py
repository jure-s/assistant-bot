from commands.utils import validate_field

def add_note_interactive(contacts):
    """
    Інтерактивне додавання нотатки до контакту.
    """
    name = validate_field("Enter the name of the contact to add a note for: ", required=True)
    contact = contacts.get(name)
    if not contact:
        return f"Contact {name} not found."

    content = validate_field("Enter the note content: ", required=True)
    tags_input = validate_field("Enter tags for the note (comma-separated): ")
    tags = tags_input.split(",") if tags_input else []

    contact.add_note(content, tags)
    return f"Note added to {name}."
