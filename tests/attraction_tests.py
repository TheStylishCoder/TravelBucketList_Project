import unittest
from models.attraction import Attraction

class TestAttraction(unittest.TestCase):

    def setUp(self):
        self.attraction = Attraction("Sensoji Temple", "Place of Worship", "Tokyo")

    def test_attraction_has_name(self):
        self.assertEqual("Sensoji Temple", self.attraction.name)