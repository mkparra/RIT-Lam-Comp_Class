#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:57:57 2020

@author: Mike Ortiz
"""
from numpy import array, meshgrid, linspace
import matplotlib.pyplot as plt
from math import sqrt, pi

def Grav_Pot(p_1,p_2): # Turning the galaxy clusters into points since we can treat them
                    # as spherical objects
    
    G=4.3*10**(-9)                                                                      #Mpc⋅M⊙^–1⋅(km/s)^2
    dist=(3.086*10**19)*((sqrt((p_1[0]-p_2[0])**2+(p_1[1]-p_2[1])**2)))  #in km
    return(-(3.086*10**19)*G*p_2[2]*(10**12)/dist)                                   #in (km/s)**2, 10**12 is mass of one galaxy, point2[2] will give the number of galaxies in disk

# step size for mesh
x = linspace(0, 10, 100)
y = linspace(0, 10, 100)

x_1, y_1 = meshgrid(x, y)
p= array([[0 for i in range(100)]for j in range(100)])

# Points of Galaxies given via the homework
g1=[7,7,400]
g2=[8,2,255]

for i in range(len(y_1)): # y coordinate
    for j in range(len(x_1)):# x coordinate
        x = x_1[0][j]
        y = y_1[i][0]
        p1 = [x,y]   # the point in consideration
        a = (x-7)**2+(y-7)**2 # initial - final for a and b
        b = (x-8)**2+(y-2)**2
        #if statments to check where the point lies and finding the potential accordingly
        if a<=9: # making sure we stay with in our coordinates given in the HW
            #this statement checks the inside the bigger the galaxy cluster
            density=400/(pi*9) #Density Mass/Volume
            num=density*(pi*a)
            p2=[7,7,num]
            Potential=Grav_Pot(p1,p2)+Grav_Pot(p1,g2)
            p[i][j]=Potential
        if b<=4: # Same for here as well       
            #this statement checks the inside the smaller galaxy cluster
            density=255/(pi*4)
            num=density*(pi*b)
            p2=[8,2,num]
            Potential=Grav_Pot(p1,p2)+Grav_Pot(p1,g1)
            p[i][j]=Potential
            
        if a>9 and b >4: # to see the points outside of the immediate cluster
            #this statement checks if the point is outside the two disks and finds potential if it is
            Potential=Grav_Pot(p1,g1)+Grav_Pot(p1,g2)
            p[i][j]=Potential
#boundary condition
for i in (0,99):
    for j in range(100):
        p[i][j]=0
        p[j][i]=0
# This is where this plot was hard to tell where the greatest potential was
# plt.contour(x_1, y_1, p, colors='Blue');
plt.contourf(x_1, y_1, p, 20, cmap='copper')
cbar=plt.colorbar();
cbar.set_label("Potenial")
plt.title('Gravity Potential of Two Galaxy Clusters')
plt.xlabel("Mpc")
plt.ylabel("Mpc")
plt.savefig("Grav_Pot For Clusters")

           
           
           
           
           
           
           