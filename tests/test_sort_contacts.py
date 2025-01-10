import unittest
from models.contact import Contact
from commands.sort_contacts import sort_contacts

class TestSortContacts(unittest.TestCase):
    def setUp(self):
        self.contacts = {
            "A": Contact("A", "1234567890"),
            "C": Contact("C", "0987654321"),
            "B": Contact("B", "1122334455")
        }

    def test_sort_by_name(self):
        result = sort_contacts(self.contacts, "name")
        self.assertEqual(result[0].name, "A")

    def test_sort_by_phone(self):
        result = sort_contacts(self.contacts, "phone")
        self.assertEqual(result[0].phone, "0987654321")
