import unittest
from unittest.mock import patch
from commands.sort_contacts import sort_contacts
from models.contact import Contact

class TestSession(unittest.TestCase):
    @patch("builtins.input", side_effect=["sort", "name", "exit"])
    def test_full_session(self, mock_input):
        contacts = {
            "John Doe": Contact("John Doe", "1234567890", email="john@example.com"),
            "Jane Doe": Contact("Jane Doe", "0987654321", email="jane@example.com"),
        }
        sorted_contacts = sort_contacts(contacts, "name")
        self.assertEqual(sorted_contacts[0].name, "Jane Doe")
        self.assertEqual(sorted_contacts[1].name, "John Doe")

    @patch("builtins.input", side_effect=["sort", "email", "exit"])
    def test_sort_by_email(self, mock_input):
        contacts = {
            "John Doe": Contact("John Doe", "1234567890", email="zjohn@example.com"),
            "Jane Doe": Contact("Jane Doe", "0987654321", email="ajane@example.com"),
        }
        sorted_contacts = sort_contacts(contacts, "email")
        self.assertEqual(sorted_contacts[0].email, "ajane@example.com")
        self.assertEqual(sorted_contacts[1].email, "zjohn@example.com")