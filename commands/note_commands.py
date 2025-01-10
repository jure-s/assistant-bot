from models.note import Note

def note_handler(command, args, data):
    if command == "add-note":
        return add_note(args, data["notes"])
    elif command == "edit-note":
        return edit_note(args, data["notes"])
    elif command == "delete-note":
        return delete_note(args, data["notes"])
    elif command == "search-note":
        return search_note(args, data["notes"])
    else:
        return "Unknown note command."

def add_note(args, notes):
    content, *tags = args
    notes.append(Note(content, tags))
    return "Note added."

def edit_note(args, notes):
    index, new_content = int(args[0]), args[1]
    if 0 <= index < len(notes):
        notes[index].content = new_content
        return "Note updated."
    return "Note not found."

def delete_note(args, notes):
    index = int(args[0])
    if 0 <= index < len(notes):
        notes.pop(index)
        return "Note deleted."
    return "Note not found."

def search_note(args, notes):
    query = args[0].lower()
    results = [str(note) for note in notes if query in note.content.lower()]
    return "\n".join(results) if results else "No notes found."