import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city_1 = City("Tokyo", "Japan")
        self.city_2 = City("Osaka", "Japan")
        self.city_3 = City("Berlin", "Germany")

    
    