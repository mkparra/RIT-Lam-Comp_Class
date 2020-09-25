#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:20:40 2020

@author: mikeortiz-parra
"""
# Problem 3 for HW 3 is writing an ODE package that has Eular's, Heun's, and the 
# explicit RK4 method. Make each step size .1, .01, or .001, number of picards 
# iterations
# lets use our inatial value problem as y = sin(x) y(0)=1
import numpy as np
from numpy import sin, cos  
import matplotlib.pyplot as plt
# here we have our start point and end point and going up by the value of .1

x_o = 0
y_o = 1
x_f = 10
n = 101
delta_x = (x_f -x_o)/(n-1)
#print(delta_x)

x = np.linspace(x_o,x_f,n)
y = np.zeros([n])
#print(y)
#print(len(x))

#print(len(y))

y[0] = y_o # STarting y[0] at one instead of 0
#print(y[0])
def Eulars(delta_x,x_func,x,y,n):
    for i in range(1,n):
        y[i] = delta_x*x_func[i-1]+ y[i-1]
        # print(y[i])
        # print(len(y))
    return x,y
x_func = sin(x)
x,y = Eulars(delta_x, x_func,x,y,n)
        

# our defined function solved analytically
def Origin(y,x):
    y_init = -cos(x)+2
    #print(y_init)
    return y_init

plt.plot(x,Origin(y,x),'r')
plt.plot(x,y,'o')
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.legend(["Original Function", "Using Eular's"], loc=3)
plt.title('Approximate Solution with Forward Eulers Method')
plt.savefig('Eulars_Method.png')
plt.show()

#%%
# Here we will be using the Heun's Method
# We can use e^x to get a good vizulization 
import numpy as np
from math import exp
import matplotlib.pyplot as plt
t_o = 0
y_o = 1
h = .1

def y_1(t,y):
    return y

def sol(t):
    return exp(t)

ysol = np.vectorize(sol) # Filling the ysol with vectorized components of the function sol which returns our exp(t).
# Basically we have our solved function to compare the Heun method against


t = np.arange(t_o,10,h)
y = np.zeros(t.size)
y[0] = y_o


#print(len(t))
#print(len(y))
def Heun(t,y): #Here we are appling our Heuns method equation to compare to our solution
    for i in range(1,t.size):
        y_interm = y[i-1] + h*y_1(t[i-1],y[i-1])
        
        y[i] = y[i-1] + (h/2)*(y_1(t[i-1],y[i-1])+y_1(t[i],y_interm))
    return t
t = Heun(t, y)    
plt.plot(t,y,'o')
plt.plot(t,ysol(t),'r')
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.legend(["Huen's", "Original Function"], loc=2)
plt.title('Approximate Solution with Huens Method')
plt.savefig('Heun_Mehtod.png')
#%%

# Here we will do a RK4 runge kutta 4th order method. exp(-2*x) - 2*y
# 
import matplotlib.pyplot as plt
import numpy as np

# Here we are making a function with open argumetns and then returning then with eval to evaluate them.
# Kinda what we talked about in class that day I asked you.
def feval(funcName, *args): 
    return eval(funcName)(*args)

# Here we are starting our bulding of the long RK4 method
def RK4thOrder(func, yinit, x_range, h):
    m = len(yinit) # Here setting the length with yint input
    n = int((x_range[-1] - x_range[0])/h) # Step size
    
    x = x_range[0]
    y = yinit
# xsol making empty then appending aka filling xsol with our range in x    
    xsol = np.empty(0) 
    xsol = np.append(xsol, x)
# Same here with y but we are filling it with a variable
    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n): #Here we are taking the equation apart and going through its function with a for loop
        k1 = feval(func, x, y)
        yp2 = y + k1*(h/2)
        k2 = feval(func, x+h/2, yp2)
        yp3 = y + k2*(h/2)
        k3 = feval(func, x+h/2, yp3)
        yp4 = y + k3*h
        k4 = feval(func, x+h, yp4)

        for j in range(m): #here we are running a loop with RK4 put back together
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])
        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])  
    return [xsol, ysol]
# Here we are making out function to compare to our RK4 methos
def myFunc(x, y):
    dy = np.zeros((len(y)))
    dy[0] = np.exp(-2*x) - 2*y[0]
    return dy

h = 0.01
x = np.array([0.0, 5])
yinit = np.array([1.0/10])

[ts, ys] = RK4thOrder('myFunc', yinit, x, h)

dt = int((x[-1]-x[0])/h)
t = [x[0]+i*h for i in range(dt+1)] 
yexact = []
for i in range(dt+1):
    ye = (1.0/10)*np.exp(-2*t[i]) + t[i]*np.exp(-2*t[i])
    yexact.append(ye)
# I wanted to see how precise this method is since originally I could not see a differnce
diff = ys - yexact
print("Maximum difference =", np.max(abs(diff)))

plt.plot(ts, ys, 'o')
plt.plot(t, yexact, 'r')
plt.xlim(x[0], x[1])
plt.legend(["4th Order RK", "Exact solution"], loc=1)
plt.title("Using the 4th Order RK method")
plt.xlabel('x values')
plt.ylabel('y values')
plt.savefig('4thOrde.png')
plt.show()





