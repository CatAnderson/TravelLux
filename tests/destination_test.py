import unittest
from models.destination import Destination

class TestDestination(unittest.TestCase):

    def setUp(self):
        self.destination1 = Destination("Tokyo", "Japan")
        self.destination2 = Destination("Osaka", "Japan")
        self.destination3 = Destination("Berlin", "Germany")

    
    def test_city_has_name(self):
        self.assertEqual("Tokyo", self.destination1.name)
        self.assertEqual("Berlin", self.destination3.name)


    def test_city_has_counrty(self):
        self.assertEqual("Japan", self.destination2.country)


    def test_city_visited_starts_false(self):
        self.assertEqual(False, self.destination1.visited)

    
    def test_can_change_city_visit_to_true(self):
        self.destination1.mark_as_visited()
        self.assertEqual(True, self.destination1.visited)
    