from models.contact import Contact

def add_note_interactive(contacts) -> str:
    """
    Інтерактивне додавання нотатки до контакту.
    """
    name = input("Enter the name of the contact to add a note for: ").strip()
    contact = contacts.get(name)
    if not contact:
        return f"Contact {name} not found."

    content = input("Enter the note content: ").strip()
    tags_input = input("Enter tags for the note (comma-separated): ").strip()
    tags = tags_input.split(",") if tags_input else []

    contact.add_note(content, tags)
    return f"Note added to {name}."