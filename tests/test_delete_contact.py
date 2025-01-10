import unittest
from unittest.mock import patch
from commands.delete_contact import delete_contact_interactive
from models.contact import Contact


class TestDeleteContact(unittest.TestCase):
    @patch("builtins.input", side_effect=["John Doe"])
    def test_delete_contact(self, mock_input):
        contacts = {
            "John Doe": Contact("John Doe", "1234567890")
        }
        message = delete_contact_interactive(contacts)
        self.assertEqual(message, "Contact John Doe deleted successfully.")
        self.assertNotIn("John Doe", contacts)

    @patch("builtins.input", side_effect=["Jane Doe"])
    def test_delete_non_existing_contact(self, mock_input):
        contacts = {}
        message = delete_contact_interactive(contacts)
        self.assertEqual(message, "Contact Jane Doe not found.")


if __name__ == "__main__":
    unittest.main()
