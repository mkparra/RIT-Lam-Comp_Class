#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:06:27 2020

@author: mikeortiz-parra
"""
# Problem 2 of HW 3. find total number denisty of N = 1 cm^-3. For convience 
# calculate the different number of densities as a function of T
#
import numpy as np
from numpy import exp 
import matplotlib.pyplot as plt
from coefficients_reader import read_coefficients

Adict = read_coefficients()

h = 6.62*10**-37 # J*s
c = 3.00*10**8 #m/s
k = 8.98*10**9 # kg*m^3*s^-2*C^-2
T = np.arange(1,5000,10) # Kelvin
E = 13.6 # eV/n^2
v_0 = E/h
J_bar = ((2*h*v_0**3)/(c))*(1/(exp((h*v_0)/(k*T))-1)) #J_bar equation
# print(J_bar)

# Load all the data that you provided
l = np.loadtxt('A_coefficients.dat',usecols = [0],skiprows=1,delimiter=',')
u = np.loadtxt('A_coefficients.dat',usecols = [1],skiprows=1,delimiter=',')
A_ul = np.loadtxt('A_coefficients.dat',usecols = [2],skiprows=1,delimiter=',')
print(A_ul)
print(u)
print(l)
g_l = 2*l**2
g_u = 2*u**2

#Solved for B_lu to check change of states in this direction
B_lu = (A_ul*c**2)/(2*h*v_0**3*g_l)* g_u

print(B_lu)
# Calling matrix
class matrix:
    def __int__(self,dims,fill=True,arr=None): # Making the constructor for the matrix
        self.rows = dims[0]
        self.cols = dims[1]
        if fill:
            self.m = [[0]*self.cols for i in range(self.rows)]
        elif self.rows*self.cols == len(arr):
            self.m = [[0]*self.cols for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    self.m[i][j] = arr[(3*i)+j]
        else:
            print(error)
            
def J_bar():            

# Here we have are making the function to check the if the energy levels are less than equal to or greater. We have this to check the values per
# process to compare. This is setting the matrices to do that.  
def Energy_State_Eq(coeffs_B_lu,J_bar,coeffs_A_ul):
    State_eq = matrix([rows,cols],fill=True)
    for row in range(State_eq.rows):
        for col in range(State_eq.cols):
            if row > col: State_Eq.m[row,col] = -coeffs_B_lu.m[row,col] * J_bar.m[row, col]
            if row < col: State_Eq.m[row, col] = -(coeffs_A_ul.m[row, col]) + coeffs_B_lu.m[row, col] * J_bar.m[row, col] 
            if row == col: State_Eq.m[row, col] = np.sum(coeffs_B_lu.m[row, col:] * J_bar.m[row, col:]) + np.sum(coeffs_B_lu.m[row, :col] * J_bar.m[row, :col]) + np.sum(coeffs_A_ul.m[row,:col])
                                                
        
            
        