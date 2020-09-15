#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:07:12 2020

@author: mikeortiz-parra
"""
# Problem 2 of HW 1 for Comp Class
# Psuedo-isothermal sphere, using your root-finding algorithms calculate the 
# width at half max.....

from Problem1_HW1_Comp_Class import Bisectional
from Problem1_HW1_Comp_Class import Secant
from Problem1_HW1_Comp_Class import Newton
import matplotlib.pyplot as plt
def g(x):
    return((1+x**2)**(-1/2)-(1/2))
def dg(x):
    return(-x/((1+x**2)**(3/2)))

def f(x):
    return (x**2-3) #Here is where you function is being defined 
l=[]
m=[]
n=[]
t=[0.1,0.001,0.0001,0.00001,0.000001,0.0000001]
for j in range(6):
    a,i=Bisectional(0,3,f,t[j])
    l.append(i)
    a,i=Newton(1.5,t[j])
    m.append(i)
    a,i=Secant(0,3,t[j])
    n.append(i)
plt.plot(t,l,"r",marker = 'o') #Bisectional
plt.plot(t,m,'b',marker = 'o') #Newton
plt.plot(t,n,'m',marker = 'o') #Secant

plt.savefig('/Users/mikeortiz-parra/Documents/Comp_Class_Lam/Problem2.png')



