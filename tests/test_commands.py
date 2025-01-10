import unittest
from unittest.mock import patch
from commands.add_contact import add_contact_interactive
from models.contact import Contact
import re

def strip_ansi(text):
    """
    Видаляє ANSI-коди кольорів із тексту.
    """
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

class TestCommands(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "John Doe",  # Name
        "1234567890",  # Phone
        "john@example.com",  # Email
        "",  # Birthday
        "123 Elm St",  # Address
        ""  # Note
    ])
    def test_add_contact(self, mock_input):
        contacts = {}
        message = add_contact_interactive(contacts)

        # Очищуємо результат від ANSI-кодів
        clean_message = strip_ansi(message)

        self.assertEqual(clean_message, "Contact John Doe added successfully.")
        self.assertIn("John Doe", contacts)
        self.assertIsInstance(contacts["John Doe"], Contact)

if __name__ == "__main__":
    unittest.main()