import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        cities = ["Tokyo", "Kyoto", "Osaka"]
        self.country = Country("Japan", cities)

    def test_country_has_name(self):
        self.assertEqual("Japan", self.country.name)