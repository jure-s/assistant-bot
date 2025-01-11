import unittest
from commands.filter_contacts import filter_contacts_by_tag, filter_contacts_by_query
from models.contact import Contact
from datetime import datetime

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.contacts = {
            "John": Contact("John", "1234567890", birthday="01.01.2000"),
            "Jane": Contact("Jane", "0987654321", birthday="15.01.1990"),
        }
        self.contacts["John"].add_note("Test note", ["tag1", "tag2"])

    def test_filter_by_tag(self):
        result = filter_contacts_by_tag(self.contacts, "tag1")
        self.assertIn("John", result)

    def test_filter_by_query(self):
        result = filter_contacts_by_query(self.contacts, "John")
        self.assertIn("John", result)

if __name__ == "__main__":
    unittest.main()
