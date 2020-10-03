import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city_1 = City("Tokyo", "Japan")
        self.city_2 = City("Osaka", "Japan")
        self.city_3 = City("Berlin", "Germany")

    
    def test_city_has_name(self):
        self.assertEqual("Tokyo", self.city_1.name)
        self.assertEqual("Berlin", self.city_3.name)


    def test_city_has_counrty(self):
        self.assertEqual("Japan", self.city_2.country)


    def test_city_visited_starts_false(self):
        self.assertEqual(False, self.city_1.visited)

    
    def test_can_change_city_visit_to_true(self):
        self.city_1.mark_as_visited()
        self.assertEqual(True, self.city_1.visited)
    