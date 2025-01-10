import unittest
from models.contact import Contact
from models.note import Note
from commands.search_contact import search_contact_interactive


class TestSearchContact(unittest.TestCase):
    def setUp(self):
        self.contacts = {
            "Ann": Contact("Ann", "0670082321", email="aa@aa.f", birthday="10.01.1987", address="AU"),
            "John": Contact("John", "0671234567", email="john@doe.com", birthday="15.05.1990", address="US"),
        }
        self.contacts["Ann"].add_note("Important note", ["tag1"])
        self.contacts["John"].add_note("Another note", ["tag2"])

    def test_search_by_name(self):
        with unittest.mock.patch("builtins.input", return_value="Ann"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("Ann", result)

    def test_search_by_phone(self):
        with unittest.mock.patch("builtins.input", return_value="067123"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("John", result)

    def test_search_by_email(self):
        with unittest.mock.patch("builtins.input", return_value="aa@aa.f"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("Ann", result)

    def test_search_by_birthday(self):
        with unittest.mock.patch("builtins.input", return_value="15.05.1990"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("John", result)

    def test_search_by_address(self):
        with unittest.mock.patch("builtins.input", return_value="US"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("John", result)

    def test_search_by_note_content(self):
        with unittest.mock.patch("builtins.input", return_value="important"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("Ann", result)

    def test_search_by_note_tag(self):
        with unittest.mock.patch("builtins.input", return_value="tag2"):
            result = search_contact_interactive(self.contacts)
            self.assertIn("John", result)

    def test_search_no_results(self):
        with unittest.mock.patch("builtins.input", return_value="nonexistent"):
            result = search_contact_interactive(self.contacts)
            self.assertEqual(result, "No contacts found.")
