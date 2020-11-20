import unittest
from types import *

import target_simulator

from target_simulator import probability
from target_simulator import hit_or_miss
from target_simulator import send_hit
from target_simulator import send_miss

class TestHitOrMiss(unittest.TestCase):
    def test_probability(self):
        ''' test that random number less than 4 is created'''
        result = probability()
        self.assertLess(result, 100)
        
    def test_hit_or_miss(self):
        result = probability()
        if result > 25:
            self.assertTrue(hit_or_miss)
        if result <= 25:
            self.assertFalse(hit_or_miss)
        
    def test_measured_force(self):
        result = send_hit()
        self.assertLess(result,50)
        
if __name__ == '__main__':
    unittest.main()