from models.contact import Contact

def edit_note_interactive(contacts) -> str:
    """
    Інтерактивне редагування нотатки контакту.
    """
    name = input("Enter the name of the contact whose note you want to edit: ").strip()
    contact = contacts.get(name)
    if not contact:
        return f"Contact {name} not found."

    index = int(input("Enter the index of the note to edit: ").strip())
    new_content = input("Enter the new content for the note: ").strip()
    try:
        contact.notes[index].content = new_content
        return f"Note updated for {name}."
    except IndexError:
        return "Note not found."