import unittest
from models.contact import Contact

class TestNotes(unittest.TestCase):
    def test_add_note(self):
        contact = Contact("John Doe", "1234567890")
        contact.add_note("Test note", ["tag1", "tag2"])
        self.assertEqual(len(contact.notes), 1)
        self.assertEqual(contact.notes[0].content, "Test note")
        self.assertEqual(contact.notes[0].tags, ["tag1", "tag2"])

    def test_delete_note(self):
        contact = Contact("John Doe", "1234567890")
        contact.add_note("Test note", ["important"])
        contact.delete_note_by_index(0)
        self.assertEqual(len(contact.notes), 0)