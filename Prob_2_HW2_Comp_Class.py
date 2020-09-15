#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:19:16 2020

@author: mikeortiz-parra
"""
# In problem 2 we will be using the NFW model and other equations to be find
# the dark matter denisty and to find mass enclosed of a galaxy. We will plot
# some of our resutls to compare them to what we are given on the HW

import numpy as np
import math as m
import matplotlib.pyplot as plt 

r_200= 2.12*10**21 # Kiloparsec to meters; I choose 300 kpc
v_200 = 1.6*10**5 # Conversion to meters/seconds
G = 6.67*10**-11 # m**3 kg**-1 s**-2
c = 15 # little confused why this is only 15..

# Numbers that I choose
r = 3.086*10**20 # meters 
v = 2.0*10**5 #meters/second
radius = [] #Making empty arrays to full in from the appends in the loops
Menc = []
vel = []
Mdark = []
# Here we are making a loop to the equations with to be able graph what we need
# and putting them in the empty array above.
for i in range(30):
    x = r/r_200
    v_sq = (v_200**2)*(1/x)*((m.log(1+(c*x))-((c*x)/(1+c*x)))/(m.log(1+(c))-((c)/(1+c))))
    Mass_enc = (r*v_sq)/G
    M_dark = (1/((x*c)*(1+(x*c))**2))*((4*m.pi*(r**3))/3) # NFW
    Mdark.append(M_dark)
    radius.append(r)
    Menc.append(Mass_enc)
    vel.append(v_sq)
    r = r+r

print(radius)
print(Menc)
print(len(radius),len(Menc))
#plt.plot(radius,Menc) # plotting mass enclosed on this one
# use these labels for radius and mass enclosed
# plt.ylabel('Mass Ecnlosed in kg')
# plt.xlabel('Radius in meters')
plt.plot(radius,Mdark) # This on plots the Dark matter content. Please use the 
#log scale on this one and not hte radius and mass enclosed. Use these labals 
#for dark matter
plt.ylabel('Mass with Dark matter content')
plt.xlabel('Radius in meters')
plt.yscale('log')
plt.xscale('log')





