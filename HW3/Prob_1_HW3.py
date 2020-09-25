#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:23:28 2020

@author: mikeortiz-parra
"""
# Problem 1 for HW 3. It is unit testing as was told! Use the Bisectional 
# Secant and Newton to make this happen
#
import numpy as np
import unittest
from math import sqrt
from Prob_3_HW2_Comp_Class import Matrix
import sys
sys.path.append(r'\Users\Mike Ortiz\Documents\GitHub\HW3\Prob_3_HW2_Comp_Class')
import scripts

#Calling the class to use unit testing
class TestMatrix(unittest.TestCase):
    def test_add(self): #Here we will be testing the addition matrix 
        a=np.array([[1,2,33],[6,4,7],[2,3,6]]) # Making arrays 3x3 to test
        b=np.array([[4,5,6],[8,19,10],[77,6,30]])
        m1=Matrix([3,3],fill=False,arr=list(a.flatten())) #Unit test matrix comparison
        m2=Matrix([3,3],fill=False,arr=list(b.flatten()))
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.assertAlmostEqual(m1.m[i][j]+m2.m[i][j],np.add(a,b)[i][j]) #Asserts to check if it is good to go.

if __name__ == '__main__':
        unittest.main()
    







