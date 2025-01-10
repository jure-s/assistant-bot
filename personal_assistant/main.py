from difflib import get_close_matches
from commands.add_contact import add_contact_interactive
from commands.edit_contact import edit_contact_interactive
from commands.delete_contact import delete_contact_interactive
from commands.search_contact import search_contact_interactive
from commands.add_note import add_note_interactive
from commands.edit_note import edit_note_interactive
from commands.delete_note import delete_note_interactive
from commands.search_notes import search_notes_interactive
from commands.show_all_contacts import show_all_contacts
from commands.help import help_command
from commands.birthdays import get_upcoming_birthdays
from commands.filter_contacts import (
    filter_contacts_by_tag,
    filter_contacts_by_birthday_range,
    filter_contacts_by_query,
)
from commands.sort_contacts import sort_contacts
from storage.file_storage import save_data, load_data
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

# Режим DEBUG
DEBUG_MODE = False

def debug_print(message):
    """
    Виводить повідомлення лише у режимі DEBUG.
    """
    if DEBUG_MODE:
        print(Fore.MAGENTA + f"DEBUG: {message}")

# Список доступних команд
AVAILABLE_COMMANDS = [
    "add-contact",
    "edit-contact",
    "delete-contact",
    "search-contact",
    "show-all",
    "add-note",
    "edit-note",
    "delete-note",
    "search-note",
    "birthdays",
    "filter-tag",
    "filter-birthday",
    "filter-query",
    "sort",
    "help",
    "exit",
    "close",
]

def suggest_command(user_input):
    """
    Пропонує найближчі команди на основі введеного користувачем тексту.
    """
    suggestions = get_close_matches(user_input, AVAILABLE_COMMANDS, n=3, cutoff=0.3)
    starts_with_matches = [cmd for cmd in AVAILABLE_COMMANDS if cmd.startswith(user_input)]
    for match in starts_with_matches:
        if match not in suggestions:
            suggestions.append(match)
    return suggestions

def main():
    data = load_data()
    contacts = data.get("contacts", {})

    print(Fore.CYAN + "Welcome to the Personal Assistant!")

    while True:
        user_input = input(Fore.YELLOW + "Enter a command (type 'help' to see all commands): ").strip().lower()

        debug_print(f"Received input '{user_input}'")

        if user_input in ["exit", "close"]:
            save_data({"contacts": contacts})
            print(Fore.GREEN + "Good bye!")
            break

        elif user_input == "help":
            print(Fore.CYAN + help_command())

        elif user_input == "show-all":
            print(Fore.CYAN + show_all_contacts(contacts))

        elif user_input == "add-contact":
            print(add_contact_interactive(contacts))

        elif user_input == "edit-contact":
            print(edit_contact_interactive(contacts))

        elif user_input == "delete-contact":
            print(Fore.GREEN + delete_contact_interactive(contacts))

        elif user_input == "search-contact":
            print(search_contact_interactive(contacts))

        elif user_input == "sort":
            field = input(Fore.YELLOW + "Enter the field to sort by (name, phone, email, birthday, address, notes, tags): ").strip().lower()
            print(Fore.CYAN + sort_contacts(contacts, field))

        elif user_input == "birthdays":
            days = input(Fore.YELLOW + "Enter the number of days: ").strip()
            try:
                days = int(days)
                print(Fore.CYAN + get_upcoming_birthdays(contacts, days))
            except ValueError:
                print(Fore.RED + "Invalid number of days. Please enter an integer.")

        elif user_input == "filter-tag":
            tag = input(Fore.YELLOW + "Enter the tag to filter by: ").strip()
            print(Fore.CYAN + filter_contacts_by_tag(contacts, tag))

        elif user_input == "filter-birthday":
            days = input(Fore.YELLOW + "Enter the number of days: ").strip()
            try:
                days = int(days)
                print(Fore.CYAN + filter_contacts_by_birthday_range(contacts, days))
            except ValueError:
                print(Fore.RED + "Invalid number of days. Please enter an integer.")

        elif user_input == "filter-query":
            query = input(Fore.YELLOW + "Enter the query to filter by: ").strip()
            print(Fore.CYAN + filter_contacts_by_query(contacts, query))

        else:
            suggestions = suggest_command(user_input)
            if suggestions:
                print(Fore.YELLOW + f"Invalid command. Did you mean: {', '.join(suggestions)}?")
            else:
                print(Fore.RED + "Invalid command. Enter 'help' to see all commands.")

if __name__ == "__main__":
    main()
