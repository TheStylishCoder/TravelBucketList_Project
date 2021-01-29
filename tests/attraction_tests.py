import unittest
from models.attraction import Attraction

class TestAttraction(unittest.TestCase):

    def setUp(self):
        self.attraction = Attraction("Sensoji Temple", "Place of Worship", "Tokyo")

    def test_attraction_has_name(self):
        self.assertEqual("Sensoji Temple", self.attraction.name)

    def test_attraction_has_category(self):
        self.assertEqual("Place of Worship", self.attraction.category)

    def test_attraction_has_city(self):
        self.assertEqual("Tokyo", self.attraction.city)

    def test_attraction_entry_fee_starts_false(self):
        self.assertEqual(False, self.attraction.entry_fee)

    def test_can_mark_entry_fee_true(self):
        self.attraction.mark_paid_entry()
        self.assertEqual(True, self.attraction.entry_fee)