# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:09:51 2020

@author: Mike Ortiz
"""

# For this problem we are going to use our RK4 ODe solver to solve
# the Static equalibrum equation that we will be appying to a 
# Neutron star
#

import numpy as np 
from numpy import linspace, array, pi, arange
import matplotlib.pyplot as plt
from Prob_3_HW3 import RK4thOrder
from scipy.integrate import odeint

# Using the scipy.intergration example as guidance
def Nuetron_Star(r,variables):
    P, M = variables 
    G = 6.67*10**-8 # dynes cm^2 g^-2 gravity in cgs
    c = 2.99*10**10 # cm*2* s^-1
    # We cant have a negative pressure so lets add zero array if
    # That happens
    if P < 0: return array([0]) 
    # Solution to solving for rho in equation 4 in the HW
    # This is known as the non relativastic degenerate electron gas
    rho = ((P)/(5.4*10**9))**(3/5)
    # Now that we have our rho we can solve for static of equilibrium
    # better yet equation 6 in the HW. We need this one for relative speeds
    dPdr = (-((G)*(M)*(rho))/(r**2))*(1+((P)/(rho*c**2)))*(1+((4*pi*r**(3)*P)/(M*c**2)))*((1-((2*G*M)/(r*c**2)))**-1)
    dMdr = 4*pi*r**2*rho
    return arange([dPdr, dMdr])
# Now we can set our ranges for radius and denstity in a for loop
# Rho is using the rho_c from the HW and Radius of star is in earth radius
for rho in linspace(10**4,10**6,10):
    Radius_Star = linspace(1*10**-4,6.37*10**8,10) 
    # Now we can import out ODE method 
    rsol, ysol = RK4thOrder('Nuetron_Star',array([1*10**-6,5.4*10**9*(rho)**(5/3)]),Radius_Star, h = 10**6)
    # Here we are plitting the output to be able to graph them with ease
    P_indices= arange(0,1274,2)
    M_indices = arange(1,1274,2)
    
print((rsol))
print((ysol[P_indices]))    
plt.plot(rsol,ysol[P_indices])
plt.title("Radius vs Pressure Graph For A Neutron Star")
plt.xlabel(r'Radius in $cm$')
plt.ylabel(r'Pressure in $dyne*cm^2$')
plt.savefig("Neutron_Star.png")