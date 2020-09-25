# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:32:24 2020

@author: Mike Ortiz
"""
# Here we will be using scipys odeint  to make sure what we hav works
#
#
#import odes
import numpy as np
from numpy import linspace, array, pi
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Prob_3_HW3 import Eulars, Heun, RK4thOrder

# A and B are contants
def Damp_Pen(t, var):
	A = 1/4 
	B = 5
	theta, w = var
	dvars_dt = np.array(-A*w - B*np.sin(theta))
	return dvars_dt

#scipy's odeint method for Pendulum 
def Pendulum_odeint(u, t, b, c):
    theta, w = u
    dydt = [w, -b*w - c*np.sin(theta)]
    return dydt

n = 1001 # Total number of steps
times = linspace(0, 10, n)
# Here we will be breaking down each plt.plot in even and odds to get accuarcy
# We will plot over each other to see the difference as well
# But I ran into issues as discussed in the PDF
x_func = Damp_Pen(times,array([pi-0.1, 0]))
print(x_func)
y = np.zeros(n)
delta_x = (10-0)/n
# t, u = Eulars(delta_x,x_func,times,y, n)
# plt.plot(t, u[linspace(0, 19998, 10000).astype(int)], label='w Eular') # odd

# plt.plot(t, u[linspace(1, 19999, 10000).astype(int)], label='theta Eular') #even 

# t,u = Heun(Damp_Pen, times, array([pi-0.1, 0]), 0.001)

# plt.plot(t, u[linspace(0, 19998, 10000).astype(int)], label='w Heun') #odd

# plt.plot(t, u[linspace(1, 19999, 10000).astype(int)], label='theta Heun') #even

# t, u = RK4thOrder(Damp_Pen, times, array([pi-0.1, 0]), 0.001)

# plt.plot(t, u[linspace(0, 19998, 10000).astype(int)], label='w RK4th') #odd

# plt.plot(t, u[linspace(1, 19999, 10000).astype(int)], label='theta RK4th') #even

u0 = [pi-0.1, 0]
t = linspace(0, 10, 101)

sol = odeint(Pendulum_odeint, u0, t, args=(0.25, 5.0)) # use odein to check vs my ODE

plt.plot(t, sol[:, 0], label='w odeint')
plt.plot(t, sol[:, 1], label='theta odeint')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Eular Heun RK4th Methods for Damped Pendulum')
plt.legend(ncol=2)
plt.savefig('Method_Damping.png')
plt.show()

