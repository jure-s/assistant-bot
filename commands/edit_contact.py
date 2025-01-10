from models.validation import validate_phone, validate_email, validate_birthday


def edit_contact_interactive(contacts):

    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        return f"Contact {name} not found."

    contact = contacts[name]

    field = input(
        "Enter the field to edit (name, phone, email, birthday, address): ").strip().lower()
    if field not in ["name", "phone", "email", "birthday", "address"]:
        return f"Invalid field. Valid fields are: name, phone, email, birthday, address."

    value = input(f"Enter the new value for {field}: ").strip()

    try:
        if field == "phone":
            value = validate_phone(value)
        elif field == "email":
            value = validate_email(value)
        elif field == "birthday":
            value = validate_birthday(value)
        contact.edit_field(field, value)
        contacts[value if field == "name" else name] = contacts.pop(name)
        return f"Contact {name} updated successfully."

    except ValueError as e:
        return f"Error: {e}"
