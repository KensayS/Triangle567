# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def test_right_triangle_1(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_2(self):
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def test_right_triangle_3(self):
        self.assertEqual(classify_triangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    def test_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_isosceles_1(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles', '2,2,3 should be isosceles')

    def test_isosceles_2(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')

    def test_scalene_1(self):
        self.assertEqual(classify_triangle(6, 7, 8), 'Scalene', '6,7,8 should be scalene')

    def test_scalene_2(self):
        self.assertEqual(classify_triangle(10, 12, 15), 'Scalene', '10,12,15 should be scalene')

    def test_invalid_1(self):
        self.assertEqual(classify_triangle(1, 1, 2), 'NotATriangle', '1,1,2 should be invalid')

    def test_invalid_2(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', '0,0,0 should be invalid')

    def test_invalid_3(self):
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput', '-1,-1,-1 should be invalid')

    def test_invalid_4(self):
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1,10,12 should be invalid')

    def test_triangle_inequality_1(self):
        self.assertEqual(classify_triangle(10, 1, 1), 'NotATriangle', '10,1,1 should be invalid due to triangle inequality')

    def test_triangle_inequality_2(self):
        self.assertEqual(classify_triangle(1, 10, 1), 'NotATriangle', '1,10,1 should be invalid due to triangle inequality')

    def test_triangle_inequality_3(self):
        self.assertEqual(classify_triangle(1, 1, 10), 'NotATriangle', '1,1,10 should be invalid due to triangle inequality')
    
    def test_side_too_large_1(self):
        self.assertEqual(classify_triangle(201, 100, 100), 'InvalidInput', '201,100,100 should be invalid due to side > 200')

    def test_side_too_large_2(self):
        self.assertEqual(classify_triangle(100, 201, 100), 'InvalidInput', '100,201,100 should be invalid due to side > 200')

    def test_side_too_large_3(self):
        self.assertEqual(classify_triangle(100, 100, 201), 'InvalidInput', '100,100,201 should be invalid due to side > 200')

    def test_side_too_large_all(self):
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput', '201,201,201 should be invalid due to all sides > 200')

    def test_non_integer_float(self):
        self.assertEqual(classify_triangle(3.5, 4, 5), 'InvalidInput', '3.5,4,5 should be invalid because 3.5 is not an integer')

    def test_non_integer_string(self):
        self.assertEqual(classify_triangle("3", 4, 5), 'InvalidInput', '"3",4,5 should be invalid because "3" is a string')

    def test_non_integer_list(self):
        self.assertEqual(classify_triangle([3], 4, 5), 'InvalidInput', '[3],4,5 should be invalid because [3] is a list')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

