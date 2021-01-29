import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        attractions = ["Sensoji Temple", "Imperial Palace", "Ghibli Museum"]
        self.city = City("Tokyo", attractions, "Japan")

    def test_city_has_name(self):
        self.assertEqual("Tokyo", self.city.name)