# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotIntegerA(self):
        self.assertEqual(classify_triangle(3,4,'five'), 'InvalidInput', 'Not a valid input')

    def testNotIntegerB(self):
        self.assertEqual(classify_triangle(3.0,4,5), 'InvalidInput', 'Not a valid input')

    def testValidTriangleA(self):
        self.assertEqual(classify_triangle(0,4,5), 'InvalidInput', '0,4,5 is not a valid triangle')

    def testValidTriangleB(self):
        self.assertEqual(classify_triangle(1,4,4), 'Isosceles', '1,4,4 is a valid triangle')
    
    def testValidTriangleC(self):
        self.assertEqual(classify_triangle(201,200,200), 'InvalidInput', '201,200,200 is not a valid triangle')
    
    def testValidTriangleD(self):
        self.assertEqual(classify_triangle(200,200,200), 'Equilateral', '200,200,200 is a valid triangle')

    def testValidTriangleE(self):
        self.assertEqual(classify_triangle(7,4,15), 'NotATriangle', '7,4,15 is not a valid triangle')

    def testValidTriangleF(self):
        self.assertEqual(classify_triangle(7,4,11), 'NotATriangle', '7,4,11 is not a valid triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(4,5,3), 'Right', '4,5,3 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(5,6,7),'Scalene', '5,6,7 is a Scalene triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(4,4,5),'Isosceles', '4,4,5 is an Isosceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)

