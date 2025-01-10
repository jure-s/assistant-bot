from commands.utils import validate_field

def delete_contact_interactive(contacts):
    """
    Інтерактивне видалення контакту.
    """
    name = validate_field("Enter the name of the contact to delete: ", required=True)
    if name in contacts:
        del contacts[name]
        return f"Contact {name} deleted successfully."
    return f"Contact {name} not found."
