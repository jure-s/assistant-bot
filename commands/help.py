def help_command():
    """
    Повертає список доступних команд.
    """
    return (
        "Supported commands:\n"
        "1. add-contact - Add a new contact.\n"
        "2. edit-contact - Edit an existing contact.\n"
        "3. delete-contact - Delete a contact.\n"
        "4. search-contact - Search for a contact.\n"
        "5. show-all - Display all contacts in the contact book.\n"
        "6. add-note - Add a note to a contact.\n"
        "7. edit-note - Edit a note for a contact.\n"
        "8. delete-note - Delete a note from a contact.\n"
        "9. search-note - Search for notes of a contact.\n"
        "10. birthdays - Show contacts with birthdays in the next N days.\n"
        "11. filter-tag - Filter contacts by note tag.\n"
        "12. filter-birthday - Filter contacts by birthday range.\n"
        "13. filter-query - Filter contacts by name, email, or phone.\n"
        "14. sort - Sort contacts by a specified field (name, phone, email, birthday, address, notes, tags).\n"
        "15. help - Show this help message.\n"
        "16. exit or close - Exit the assistant."
    )