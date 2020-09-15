#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:20:40 2020

@author: mikeortiz-parra
"""
# Problem 3 for HW 3 is writing an ODE package that has Eular's, Heun's, and the 
# explicit RK4 method. Make each step size .1, .01, or .001, number of picards 
# iterations
# lets use our inatial value problem as y = -y+sin(x) y(0)=1
import numpy as np 
from math import sin
import matplotlib.pyplot as plt


# here we have our start point and end point and going up by the value of .1

x_o = 0
y_o = 1
x_f = 10
n = 101
delta_x = (x_f -x_o)/(n-1)
print(delta_x)

x = np.linspace(x_o,x_f,n)
y = np.zeros([n])
print(len(x))
print(len(y))

y[0] = y_o
print(y[0])
for i in range(1,n):
    y[i] = delta_x*(sin(x[i-1])-y[i-1])+ y[i-1]
    print(y[i])
    print(len(y))

plt.plot(x,y)
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.title('Approximate Solution with Forward Eulers Method')
plt.show()

#%%
# Here we will be using the Heun's Method
# We can use e^x to get a good vizulization 
import numpy as np
from math import exp
import matplotlib.pyplot as plt
t_o = 0
y_o = 1
h = .01

def y_1(t,y):
    return y

def sol(t):
    return exp(t)

ysol = np.vectorize(sol)


t = np.arange(0,10,h)
y = np.zeros(t.size)
y[0] = y_o

print(len(t))
print(len(y))

for i in range(i,t.size):
    y_interm = y[i-1] + h*y_1(t[i-1],y[i-1])
    
    y[i] = y[i-1] + (h/2)*(y_1(t[i-1],y[i-1])+y_1(t[i],y_interm))

plt.plot(t,y,'-r',y,ysol,'-b')  







