from commands.utils import validate_field

def edit_note_interactive(contacts):
    """
    Інтерактивне редагування нотатки контакту.
    """
    name = validate_field("Enter the name of the contact whose note you want to edit: ", required=True)
    contact = contacts.get(name)
    if not contact:
        return f"Contact {name} not found."

    try:
        index = int(validate_field("Enter the index of the note to edit: ", required=True))
        new_content = validate_field("Enter the new content for the note: ", required=True)
        contact.notes[index].content = new_content
        return f"Note updated for {name}."
    except IndexError:
        return f"Note with index {index} not found for contact {name}."
    except ValueError:
        return "Invalid input. Please provide a valid index and content."
