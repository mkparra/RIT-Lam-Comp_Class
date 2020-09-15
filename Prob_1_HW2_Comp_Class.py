#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:04:41 2020

@author: mikeortiz-parra
"""
# Problem 1 HW2 Comp Class
# Write a numerical calculus library. one that can perform at least one 
# derivative and at least three intergrations including Midpoint rule, 
# trapaziod method, and simpsons rule

# Starting with Derivitive
import matplotlib.pyplot as plt
import numpy as np 
def Symmetric(x): # Writing in equation centered differnce; E.C.D
    h = 1e-10 #smaller the number the bigger the accuracy
    return ((fun(x+h)-fun(x-h))/(2*h))
def fun(x): # Putting in our equation that we want to take derivitive of
    return (x**2)-45

def dfun(x): # Taking derivitive by hand and putting it here to check results
    return 2*x


x = np.arange(0,10,1) # out range of values to check in our E.C.D
dx = Symmetric(x)  # Calling out funtion to be able to graph with range values

# Plotting to see if our equation worked and printing out numbers
plt.plot(x,fun(x),label='OG Func')
plt.plot(x,dfun(x),label='Dv Func',linestyle='--',zorder=10)
plt.plot(x,dx,label='Derivative',zorder=9)
plt.legend()
plt.show()

# Printing out numbers has shown us that this in deed works, but I have
# noticed that when you pick a bigger number the outputs become the same.
# Smaller h means you get to see the differene at more sig figs
print(dfun(x))
print(dx)

#%%
# Here we will check the trapaziod method to be able to check the area under
# the curve but in this case we will check a sin going to pi/2 to evalute it.
# We then will compare to other methods and see whats up.
#

from math import sin,pi
import matplotlib.pyplot as plt

def Trap(f, a, b, n): #setting the function 
    x = 0 #Using sin so hitting once for pi/2 and checking approx value for that
    if b > a: # Making sure we get the postive number in the denominator 
        h = (b-a)/float(n) #step size h, from input values divided by n
    else:
        h = (a-b)/float(n)

    for i in range (0, n): # Putting it in a loop
        k = 0.5 * h * ( f(a + i*h) + f(a + (i+1)*h) )
        x = x + k

    return x


print ( Trap(sin, 0, 0.5*pi, 100) )
print ( Trap(abs, 0, 1, 100) )


#%%
# Here we are testing out the Simpson rule. Here we will check the accuracy of
# the rule by printing out the same number and checking sin at pi/2 again and
# see the difference in accuracy

import matplotlib.pyplot as plt
from math import sin,pi

def Simp(f, a, b, n):
    h=(b-a)/n  #step size h, from input values divided by n
    d=0
    x=a + h
    for i in range(1,n // 2 + 1):
        d += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,n // 2):
        d += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+d)

def func(x): 
    return x

print(Simp(sin, 0, .5*pi, 100))
print(Simp(func,0,1,100))

# We can see here through the printed values that Simp is the most accurate

#%%


def midpoint(f, a, b, n):
    h = (b-a)/float(n)
    x_0= a
    x_1 = x_0+h
    sum = f((a)+(x_1)/2)*h
    for i in range(n-1):
        x_1 = x_0+h
        x_0=x_1
        a_2 = f(x_1+(h/2))*h
        sum_1 = a_2 + sum 
        
    print(sum_1)



    


        






