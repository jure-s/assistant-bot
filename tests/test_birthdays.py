import unittest
from datetime import datetime
from commands.birthdays import get_upcoming_birthdays
from models.contact import Contact

class TestBirthdays(unittest.TestCase):
    def setUp(self):
        self.contacts = {
            "John": Contact("John", "1234567890", birthday="01.01.2000"),
            "Jane": Contact("Jane", "0987654321", birthday="15.01.1990"),
        }

    def test_get_upcoming_birthdays(self):
        result = get_upcoming_birthdays(self.contacts, 365)
        self.assertIn("John", result)
        self.assertIn("Jane", result)
