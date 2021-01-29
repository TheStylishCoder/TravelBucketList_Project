import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review("Great Day Out", "Beautiful architecture and gardens. Found a great place for lunch nearby.", "Sensoji Temple")

    def test_review_has_title(self):
        self.assertEqual("Great Day Out", self.review.title)

    def test_review_has_content(self):
        self.assertEqual("Beautiful architecture and gardens. Found a great place for lunch nearby.", self.review.content)

    def test_has_attraction(self):
        self.assertEqual("Sensoji Temple", self.review.attraction)