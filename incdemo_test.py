# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:06:16 2018

@author: eugenr
"""

import unittest
from inc import inc

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(inc(0), 1)
        self.assertEqual(inc(100), 101)
        self.assertEqual(inc(1), 2)
        self.assertEqual(inc(-1), 0)
        
if __name__ == '__main__':
    unittest.main()
    
