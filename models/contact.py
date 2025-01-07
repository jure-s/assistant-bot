from datetime import datetime

class Note:
    def __init__(self, content, tags):
        self.content = content
        self.tags = tags

    def __str__(self):
        tags_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"Note: {self.content}, Tags: {tags_str}"

class Contact:
    def __init__(self, name, phone, email=None, birthday=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.notes = []

        if isinstance(birthday, str):
            self.birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
        else:
            self.birthday = birthday

    def __str__(self):
        formatted_birthday = self.birthday.strftime("%d.%m.%Y") if self.birthday else "N/A"
        notes_str = "\n    ".join(str(note) for note in self.notes) if self.notes else "No notes"
        return (f"Name: {self.name}, Phone: {self.phone}, Email: {self.email or 'N/A'}, "
                f"Birthday: {formatted_birthday}, Address: {self.address or 'N/A'}, Notes:\n    {notes_str}")

    def add_note(self, content, tags):
        self.notes.append(Note(content, tags))

    def edit_field(self, field, value):
        if hasattr(self, field):
            setattr(self, field, value)
        else:
            raise AttributeError(f"Field '{field}' does not exist.")

    def delete_note_by_index(self, index):
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
        else:
            raise IndexError("Invalid note index.")
