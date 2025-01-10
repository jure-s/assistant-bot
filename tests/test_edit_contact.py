import unittest
from unittest.mock import patch
from commands.edit_contact import edit_contact_interactive
from models.contact import Contact


class TestEditContact(unittest.TestCase):
    @patch("builtins.input", side_effect=["John", "email", "john@example.com"])
    def test_edit_contact_email(self, mock_input):
        contacts = {"John": Contact(
            "John", "1234567890", email="old@example.com")}
        message = edit_contact_interactive(contacts)
        self.assertEqual(contacts["John"].email, "john@example.com")
        self.assertIn("updated successfully", message)

    @patch("builtins.input", side_effect=["John", "phone", "0987654321"])
    def test_edit_contact_phone(self, mock_input):
        contacts = {"John": Contact(
            "John", "1234567890", email="old@example.com")}
        message = edit_contact_interactive(contacts)
        self.assertEqual(contacts["John"].phone, "0987654321")
        self.assertIn("updated successfully", message)

    @patch("builtins.input", side_effect=["Jane", "name", "Jane Doe"])
    def test_edit_non_existing_contact(self, mock_input):
        contacts = {"John": Contact(
            "John", "1234567890", email="old@example.com")}
        message = edit_contact_interactive(contacts)
        self.assertIn("not found", message)
