import unittest
import currency_ingester as ci
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def test_get_countries(self):
        ingester = ci.ingester()
        countries = ingester.get_conversion_rate()
        pprint(countries)


if __name__ == '__main__':
    unittest.main()
