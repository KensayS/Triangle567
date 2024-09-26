# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def test_right_triangle_1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_2(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def test_right_triangle_3(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    def test_equilateral(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_isosceles_1(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 should be isosceles')

    def test_isosceles_2(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')

    def test_scalene_1(self):
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene', '6,7,8 should be scalene')

    def test_scalene_2(self):
        self.assertEqual(classifyTriangle(10, 12, 15), 'Scalene', '10,12,15 should be scalene')

    def test_invalid_1(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1,1,2 should be invalid')

    def test_invalid_2(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 should be invalid')

    def test_invalid_3(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput', '-1,-1,-1 should be invalid')

    def test_invalid_4(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 should be invalid')

    def test_non_numeric_1(self):
        with self.assertRaises(TypeError):
            classifyTriangle('a', 3, 4)

    def test_non_numeric_2(self):
        with self.assertRaises(TypeError):
            classifyTriangle(3, 'b', 5)

    def test_non_numeric_3(self):
        with self.assertRaises(TypeError):
            classifyTriangle(3, 4, 'c')

    def test_non_numeric_4(self):
        with self.assertRaises(TypeError):
            classifyTriangle([1, 2, 3], 4, 5)

    def test_non_numeric_5(self):
        with self.assertRaises(TypeError):
            classifyTriangle(None, 4, 5)

    def test_non_numeric_6(self):
        with self.assertRaises(TypeError):
            classifyTriangle(3.0, "4.0", 5.0)

    def test_triangle_inequality_1(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 should be invalid due to triangle inequality')

    def test_triangle_inequality_2(self):
        self.assertEqual(classifyTriangle(1, 10, 1), 'NotATriangle', '1,10,1 should be invalid due to triangle inequality')

    def test_triangle_inequality_3(self):
        self.assertEqual(classifyTriangle(1, 1, 10), 'NotATriangle', '1,1,10 should be invalid due to triangle inequality')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

