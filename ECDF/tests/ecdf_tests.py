"""Unit test for ecdf, an empirical cumulative distribution function finder."""  

import ecdf.ecdf
import unittest

class TestGoodInput(unittest.TestCase):
    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman1.to_roman(integer)
            self.assertEqual(numeral, result)

class TestBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000) 

    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 0)  

if __name__ == '__main__':
    unittest.main()
