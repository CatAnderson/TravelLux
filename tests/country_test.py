import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country_1 = Country("Japan", "Asia")
        self.country_2 = Country("Germany", "Europe")


    def test_country_has_name(self):
        self.assertEqual("Japan", self.country_1.name)


    def test_country_has_continent(self):
        self.assertEqual("Europe", self.country_2.continent)