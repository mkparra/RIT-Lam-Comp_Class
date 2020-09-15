#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:35:12 2020

@author: mikeortiz-parra
"""
# Problem 4. Using Gaussian Lens equation that if you have a light ray hitting 
# x, and you know the other parameters of the lens(a, N_o, D etc).

import math
from Problem1_HW1_Comp_Class import Bisectional  
from astropy import units as u
import matplotlib.pyplot as plt

#Converting units here
D=1*u.kiloparsec
D=D.to(u.cm)
#print(D)
a = 1*u.AU
a=a.to(u.cm)
#print(a)
lam = 21*u.cm
#print(lam)
N_o=0.01*u.pc/u.cm**3
N_o=N_o.to(u.cm**(-2))
# #print(N_0)
r_e =2.83*10**(-13)*u.cm
# #print(r_e)
c=(lam**2)*r_e*N_o*D/(math.pi*a**2)

# Making a function inside of a function with solved parts of the plug and chug part
def f(x_prime,c):
    def y(x):
        return(x*(1+(c*(1+x**2)**2))-x_prime)
    return(y)

# Empty arrays to store numbers in my for loop for "months"
x_0 = []
x_1 = []

# Here making a for loop to be able to go around our 'orbit' and to see where we are at
for i in range(12):
    x_prime = 1 +math.cos(i*math.pi*1/6)
    x_1.append(x_prime)
    z,q=Bisectional(0,2,f(x_prime,c))
    x_0.append(z)
print(x_0)
print(x_1)
plt.clf()   # Plotting the mutiple results on graph
plt.gca().axes.get_yaxis().set_visible(False)
plt.title('Lens Equation In One Year of Traval')
plt.xlabel('How far away are you the Observer')
for i in range(12):
    plt.plot([x_1[i],x_0[i],0],[-2,0,2])
plt.savefig("/Users/mikeortiz-parra/Documents/Comp_Class_Lam/HW1_problem3.png")