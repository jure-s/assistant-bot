import unittest
from models.contact import Contact
from datetime import datetime


class TestContact(unittest.TestCase):
    def test_create_contact_with_birthday(self):
        contact = Contact("John Doe", "1234567890", birthday="01.01.2000")
        self.assertEqual(contact.birthday, datetime.strptime(
            "01.01.2000", "%d.%m.%Y").date())

    def test_contact_str_with_birthday(self):
        contact = Contact("Jane Doe", "0987654321", birthday="01.01.2000")
        contact_str = str(contact)
        self.assertIn("01.01.2000", contact_str)

    def test_edit_contact_birthday(self):
        contact = Contact("Jane Doe", "0987654321", birthday="01.01.1990")
        contact.edit_field("birthday", datetime.strptime(
            "31.12.1999", "%d.%m.%Y").date())
        self.assertEqual(contact.birthday, datetime.strptime(
            "31.12.1999", "%d.%m.%Y").date())
