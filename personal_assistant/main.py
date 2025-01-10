import pickle
from commands.add_contact import add_contact_interactive
from commands.edit_contact import edit_contact_interactive
from commands.delete_contact import delete_contact_interactive
from commands.sort_contacts import sort_contacts
from commands.filter_contacts import filter_contacts_by_tag, filter_contacts_by_birthday_range, filter_contacts_by_query
from commands.notes import add_note_interactive, edit_note_interactive, delete_note_interactive, search_note_interactive
from commands.birthdays import get_upcoming_birthdays

DEBUG = False

def debug_print(message):
    if DEBUG:
        print(f"DEBUG: {message}")

def load_contacts(filename="contacts.pkl"):
    try:
        with open(filename, "rb") as file:
            debug_print(f"Contacts loaded from {filename}")
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        debug_print("No existing contact book found. Starting fresh.")
        return {}

def save_contacts(contacts, filename="contacts.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(contacts, file)
        debug_print(f"Contacts saved to {filename}")

def main():
    contacts = load_contacts()

    while True:
        command = input("Enter a command (type 'help' to see all commands): ").strip().lower()
        debug_print(f"Received input '{command}'")

        if command in ("exit", "close"):
            save_contacts(contacts)
            print("Data saved.\nGood bye!")
            break

        if command == "help":
            print("Supported commands:")
            print("1. add-contact - Add a new contact.")
            print("2. edit-contact - Edit an existing contact.")
            print("3. delete-contact - Delete a contact.")
            print("4. search-contact - Search for a contact.")
            print("5. show-all - Display all contacts in the contact book.")
            print("6. add-note - Add a note to a contact.")
            print("7. edit-note - Edit a note for a contact.")
            print("8. delete-note - Delete a note from a contact.")
            print("9. search-note - Search for notes of a contact.")
            print("10. birthdays - Show contacts with birthdays in the next N days.")
            print("11. filter-tag - Filter contacts by note tag.")
            print("12. filter-birthday - Filter contacts by birthday range.")
            print("13. filter-query - Filter contacts by name, email, or phone.")
            print("14. sort - Sort contacts by a specified field (name, phone, email, birthday, address, notes, tags).")
            print("15. help - Show this help message.")
            print("16. exit or close - Exit the assistant.")

        elif command == "show-all":
            if not contacts:
                print("No contacts to show.")
            else:
                for contact in contacts.values():
                    print(contact)

        elif command == "sort":
            field = input("Enter the field to sort by (name, phone, email, birthday, address, notes, tags): ").strip().lower()
            contacts = sort_contacts(contacts, field)
            save_contacts(contacts)  # Зберігаємо порядок сортування
            for contact in contacts.values():
                print(contact)

        elif command == "edit-contact":
            print(edit_contact_interactive(contacts))

        # Інші команди аналогічні
        else:
            print("Invalid command. Enter 'help' to see all commands.")