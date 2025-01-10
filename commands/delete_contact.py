from commands.utils import validate_field


def delete_note_interactive(contacts):

    name = validate_field(
        "Enter the name of the contact whose note you want to delete: ", required=True)

    contact = contacts.get(name)

    if not contact:
        return f"Contact {name} not found."

    note_text_or_tag = validate_field(
        "Enter the text or tag of the note to delete: ", required=True)

    for index, note in enumerate(contact.notes):
        if note_text_or_tag in note.content or note_text_or_tag in note.tags:
            contact.delete_note(index)
            return f"Note '{note.content}' deleted for {name}."

    return f"No note found with text or tag '{note_text_or_tag}' for contact {name}."
