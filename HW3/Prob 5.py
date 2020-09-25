# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:18:10 2020

@author: Mike Ortiz
"""
import numpy as np
from numpy import array, linspace, cos, sin, exp, pi
import matplotlib.pyplot as plt
from Prob_3_HW3 import Eulars, Heun, RK4thOrder



def stiff(t, y):
	lambd = 100 # stiffness high ODE capility input
	dy_dt = array(-lambd*(y - cos(t)))
	return dy_dt

def stiff_real(t):
	lambd = 100 # stiffness high ODE capility input
	return -lambd**2/(1+lambd**2)*exp(-lambd*t) + lambd/(1+lambd**2)*sin(t) + lambd**2/(1+lambd**2)*cos(t)
# Tried to make the arguments fit here but no bueno
n = .001
times = linspace(0, 10, 101)
x_func = stiff(times,array([pi-0.1, 0]))
print(x_func)
y = np.zeros(n)
delta_x = (10-0)/n
# print(x_func)
# Where I ran into issues
t, y = Eulars(stiff, times, array([1e-6]),1e-3)
plt.plot(t, y, label='Eulars')
t, u = Heun(stiff, times, array([1e-6]), 1e-3)
plt.plot(t, u, label='Heun')
t, u = RK4thOrder(stiff, times, array([1e-6]), 1e-3)
plt.plot(t, y, label='rk4')
plt.plot(t, stiff_real(t), label='true')
plt.legend()
plt.xlabel('Times (s)')
plt.ylabel('Amplitude')
plt.title('Test of stiff ODE solving capability')
plt.savefig('/Users/Mike Ortiz/Documents/GitHub/RIT-Lam-Comp_Class/HW3/Stiff.png')
plt.show()