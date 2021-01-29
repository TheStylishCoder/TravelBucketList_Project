import unittest
from models.country import Country


class TestCountry(unittest.TestCase):

    def setUp(self):
        cities = ["Tokyo", "Kyoto", "Osaka"]
        self.country = Country("Japan", cities)

    def test_country_has_name(self):
        self.assertEqual("Japan", self.country.name)

    def test_country_has_cities(self):
        self.assertEqual(3, len(self.country.cities))

    def test_country_visited_starts_false(self):
        self.assertEqual(False, self.country.visited)

    def test_country_wishlist_starts_false(self):
        self.assertEqual(False, self.country.wishlist)

    def test_can_mark_visited(self):
        self.country.mark_visited()
        self.assertEqual(True, self.country.visited)
    
    def test_can_mark_wishlist(self):
        self.country.mark_wishlist()
        self.assertEqual(True, self.country.wishlist)