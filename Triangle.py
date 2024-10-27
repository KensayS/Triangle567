# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple Python program to classify triangles.

@author: jrr
@author: rk
"""

def classify_triangle(a, b, c):
    """
    Classifies a triangle given the lengths of its three sides.

    Args:
        a, b, c (int): Lengths of the triangle's sides.

    Returns:
        str: The type of triangle: 'Equilateral', 'Isosceles', 'Scalene', 'Right', 'NotATriangle', 
             or 'InvalidInput'.
    """
    # Ensure all inputs are integers within a valid range
    if not all(isinstance(x, int) and 0 < x <= 200 for x in (a, b, c)):
        return 'InvalidInput'

    # Sort the sides so that c is always the largest
    a, b, c = sorted((a, b, c))

    # Check for the triangle inequality
    if a + b <= c:
        return 'NotATriangle'

    # Determine the type of triangle
    if a == b == c:
        return 'Equilateral'
    if a**2 + b**2 == c**2:
        return 'Right'

    return 'Scalene' if len({a, b, c}) == 3 else 'Isosceles'
