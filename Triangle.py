# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk

UPDATES October 7, 2020:
@author: zg

Updates to code per pylint output. Functions remain the same,
but did remove some of the older docstrings.
"""

def classify_triangle(side_a: int,side_b: int,side_c: int) -> str:

    """
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """

    #create blank string
    outputted_triangle: str = ''

    #verify that all 3 inputs are integers
    #Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(side_a,int) and isinstance(side_b,int) and isinstance(side_c,int)):
        outputted_triangle = 'InvalidInput'
        return outputted_triangle

    #require that the input values be > 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        outputted_triangle = 'InvalidInput'
        return outputted_triangle

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        outputted_triangle = 'InvalidInput'
        return outputted_triangle

    #This information was not in the requirements spec but
    #is important for correctness
    #the sum of any two sides must be strictly less than the third side
    #of the specified shape is not a triangle
    if side_a >= (side_b + side_c) or side_b >= (side_a + side_c) or side_c >= (side_a + side_b):
        outputted_triangle = 'NotATriangle'
        return outputted_triangle

    #now we know that we have a valid triangle
    #sort the sides by least to greatest to help with right triangle classification
    side_a,side_b,side_c = sorted([side_a,side_b,side_c])
    if side_a == side_b and side_b == side_c:
        outputted_triangle = 'Equilateral'
    elif ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2):
        outputted_triangle = 'Right'
    elif (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
        outputted_triangle = 'Scalene'
    else:
        outputted_triangle = 'Isosceles'

    #return outputted triangle
    return outputted_triangle
    