from colorama import Fore, Style

def help_command():
    """
    Повертає список доступних команд зі структурою, кольорами, розділеними за функціоналом, і покращеними стилями.
    """
    return (
        f"{Fore.WHITE}{Style.BRIGHT}Supported commands:\n\n"
        f"{Fore.WHITE}{Style.BRIGHT}Contacts:\n"
        f"{Fore.YELLOW}1. add-contact{Fore.LIGHTBLACK_EX} - Add a new contact.\n"
        f"{Fore.BLUE}2. edit-contact{Fore.LIGHTBLACK_EX} - Edit an existing contact.\n"
        f"{Fore.RED}3. delete-contact{Fore.LIGHTBLACK_EX} - Delete a contact.\n"
        f"{Fore.GREEN}4. search-contact{Fore.LIGHTBLACK_EX} - Search for a contact.\n"
        f"{Fore.CYAN}5. show-all{Fore.LIGHTBLACK_EX} - Display all contacts in the contact book.\n\n"
        f"{Fore.WHITE}{Style.BRIGHT}Notes:\n"
        f"{Fore.YELLOW}6. add-note{Fore.LIGHTBLACK_EX} - Add a note to a contact.\n"
        f"{Fore.BLUE}7. edit-note{Fore.LIGHTBLACK_EX} - Edit a note for a contact.\n"
        f"{Fore.RED}8. delete-note{Fore.LIGHTBLACK_EX} - Delete a note from a contact.\n"
        f"{Fore.GREEN}9. search-note{Fore.LIGHTBLACK_EX} - Search for notes across all contacts.\n\n"
        f"{Fore.WHITE}{Style.BRIGHT}Filters:\n"
        f"{Fore.GREEN}10. filter-tag{Fore.LIGHTBLACK_EX} - Filter contacts by note tag.\n"
        f"{Fore.GREEN}11. filter-birthday{Fore.LIGHTBLACK_EX} - Filter contacts by specific birthday.\n"
        f"{Fore.GREEN}12. filter-query{Fore.LIGHTBLACK_EX} - Filter contacts by name, email, or phone.\n\n"
        f"{Fore.WHITE}{Style.BRIGHT}General:\n"
        f"{Fore.CYAN}13. sort{Fore.LIGHTBLACK_EX} - Sort contacts by a specified field (name, phone, email, birthday, address, notes, tags).\n"
        f"{Fore.GREEN}14. help{Fore.LIGHTBLACK_EX} - Show this help message.\n"
        f"{Fore.RED}15. exit{Fore.LIGHTBLACK_EX} or {Fore.RED}close{Fore.LIGHTBLACK_EX} - Exit the assistant.\n"
    )
