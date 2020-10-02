# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:41:25 2020

@author: Mike Ortiz
"""

# For this problem we are going to use our RK4 ODe solver to solve
# the Static equalibrum equation that we will be appying to a 
# white dwarf
#

import numpy as np 
from numpy import linspace, array, pi, arange
import matplotlib.pyplot as plt
from Prob_3_HW3 import RK4thOrder
from scipy.integrate import odeint

# Using the scipy.intergration example as guidance
def White_Dwarfs(r,variables):
    M, P = variables
    G = 6.67*10**-8 # dynes cm^2 g^-2 gravity in cgs
    # We cant have a negative pressure so lets add zero array if
    # That happens
    if P < 0: return array([0]) 
    # Solution to solving for rho in equation 4 in the HW
    # This is known as the non relativastic degenerate electron gas
    rho = ((P)/(1.0*10**13))**(3/5)*2
    # Now that we have our rho we can solve for static of equilibrium
    # better yet equation 1 and 2
    dPdr = -((G)*(M)*(rho))/(r**2)
    dMdr = 4*pi*r**2*rho
    return array([dPdr, dMdr])
# Now we can set our ranges for radius and denstity in a for loop
# Rho is using the rho_c from the HW and Radius of star is in earth radius
for rho in linspace(10**4,10**6,10):
    Radius_Star = linspace(1*10**-4,6.37*10**8,10) 
    # Now we can import out ODE method 
    rsol, ysol = RK4thOrder('White_Dwarfs',array([1e-6,1.0*10**13*(rho/2)**(5/3)]),Radius_Star,h = 10**6) 
    P_indices= arange(0,1274,2)
    M_indices = arange(1,1274,2)
    P = ysol[P_indices]
    # Was trying to make it work with no nans since I though that was causing my error
    # P = P[~np.isnan(P)]
    # r = rsol
    # r = r[~np.isnan(P)]
    # print(rsol)
    # print(M_indices)

print(len(rsol))
print(len(ysol[P_indices]))
plt.plot(rsol,ysol[P_indices]) 
plt.xlabel('radius in cm')
plt.ylabel('Pressure in Dynes cm^2')
plt.title('White Dwarf Mass-Radius Curve :(')
plt.savefig('White Dwarf')

    
    

