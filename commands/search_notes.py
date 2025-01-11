def search_notes_across_contacts(contacts):
    """
    Пошук нотаток по всіх контактах.
    """
    query = input("Enter the search query: ").strip().lower()
    results = []

    for contact in contacts.values():
        for note in contact.notes:
            if query in note.content.lower() or query in [tag.lower() for tag in note.tags]:
                results.append(f"{contact}")

    return "\n".join(results) if results else "No notes found matching your query."
