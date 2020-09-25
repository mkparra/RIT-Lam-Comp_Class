#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:21:27 2020

@author: mikeortiz-parra
"""
# Write the library for the three root-finding problem algorithms in class,
# Bisectional, Newton, Secant. Make it take functions rather than data points

# from Problem_2_Comp_Class import f  #Doing these imports so I dont have to 
# to do it again on a different script, Calling it to make it easier

#from Problem_2_Comp_Class import g  # Same for doing it here in imort g

#from Problem_2_Comp_Class import dg

def Bisectional(a,b,f,t = .00001):
    x_0 = a
    x_1 = b 
    x_2 = (x_1 + x_0) * (1/2) # setting threshold inbetween both end points
    y_0 = f(x_0)
    y_1 = f(x_1)
    y_2 = f(x_2)
    i = 1
    while ((x_2-x_1)/(x_1))>t or ((x_2-x_1)/(x_1))<-t: #We use this here to come in to our threshold from either end
        if y_2*y_0<0: #Using an if statment to stop where we deem reasonable into getting to the threshold
            x_0 = x_0
            x_1 = x_2
            x_2 = (x_1+x_0)*(1/2) #Threshold for the if statment
            y_0 = f(x_0)
            y_1 = f(x_1)
            y_2 = f(x_2)
            i = i + 1
        else:          # If the conditions are not satisfied this should help us
            x_0 = x_2
            x_1 = x_1
            x_2 = (x_1+x_0)*(1/2)
            y_0 = f(x_0)
            y_1 = f(x_1)
            y_2 = f(x_2)
            i = i + 1
            
    return(x_2,i)


#Secant Method 
def Secant(a,b,t = .00001):
    x_0 = a
    x_1 = b
    y_0 = x_0**-3
    y_1 = x_1**-3
    x_2 = x_1 - (float(x_1-x_0)/(y_1 - y_0))*y_1
    y_2 = x_2**2-3
    i = 1
    while ((x_2-x_1)/x_1)>t or ((x_2-x_1)/x_1)<-t: 
        if y_2*y_1<0:
            x_0 = x_1
            x_1 = x_2
            y_0 = x_0**-3
            y_1 = x_1**-3
            x_2 = x_1 - (float(x_1-x_0)/(y_1 - y_0))*y_1
            y_2 = x_2**2-3
            i = i + 1
        else:
            x_0 = x_1
            x_1 = x_2
            y_0 = x_0**-3
            y_1 = x_1**-3
            x_2 = x_1 - (float(x_1-x_0)/(y_1 - y_0))*y_1
            y_2 = x_2**2-3
            i = i +1
            
    return(x_2,i)
            
    
def Newton(a,t = .00001):
    x_1 = a-(((1+a**2)**(-1/2)-(1/2)))/(-a/((1+a**2)**(3/2)))
    i = 1 
    while (x_1-a)/a > t or (x_1-a)/a < -t:
        a = x_1 
        x_1 = a-(((1+a**2)**(-1/2)-(1/2)))/(-a/((1+a**2)**(3/2)))
        i = i + 1
    return(x_1,i)
    
    
    
    
    
    