import unittest
from city_functions import city_country

class CitysTestCase(unittest.TestCase):
    """Tests for "city_functions.py"""

    def test_city_country(self):
        """Does input like 'Köln Germany' work?"""
        formatted_city = city_country("köln", "germany")
        self.assertEqual(formatted_city, "Köln, Germany")

    def test_city_country_population(self):
        "Does input like 'köln. germany, 2000000' work?"
        formatted_city = city_country("köln", "germany", "2000000")
        self.assertEqual(formatted_city, "Köln, Germany - population 2000000")

unittest.main()