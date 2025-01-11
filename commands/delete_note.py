from commands.utils import validate_field
from colorama import Fore

def delete_note_interactive(contacts):
    """
    Інтерактивне видалення нотатки контакту.
    """
    name = validate_field("Enter the name of the contact whose note you want to delete: ", required=True)
    contact = contacts.get(name)
    if not contact:
        return Fore.RED + f"Contact {name} not found."

    note_text_or_tag = validate_field("Enter the text or tag of the note to delete: ", required=True)

    # Пошук нотатки за текстом або тегами
    for index, note in enumerate(contact.notes):
        if note_text_or_tag in note.content or note_text_or_tag in note.tags:
            contact.delete_note_by_index(index)  # Використання правильного методу
            return Fore.GREEN + f"Note '{note.content}' deleted for {name}."

    return Fore.RED + f"No note found with text or tag '{note_text_or_tag}' for contact {name}."
