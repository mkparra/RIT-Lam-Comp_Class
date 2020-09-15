#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:07:39 2020

@author: mikeortiz-parra
"""
# Problem 6 for Comp Class: Write a library for piecewise liner interpolation,
# given a set of x and y data points. This should return...
# from scipy import interpolate
# import numpy as np
#%%
import matplotlib.pyplot as plt
from Problem_5_HW1_Comp_Class import inter

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

N_e = [0,0,.001,.008,.030,.065,.103,.130,.140,.132,.113,.089,.066,.046,.030,.019,.012,.007,.004,.002,.001]

x_new = [.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5]

y_new = []



for i in range(len(x_new)):
    d = inter(x[i+1],N_e[i+1],x[i],N_e[i])
    y_new.append(d(x_new[i]))
print(y_new)



# y_new = 0*(1-x_d)+.001*x_d
#print(x)
#print(N_e)
plt.plot(x,N_e,'r',x_new,y_new,marker='o')
plt.savefig('/Users/mikeortiz-parra/Documents/Comp_Class_Lam/H1_Problem6.png')
# print(y_new)



#print(y_new)
#print(x_new)


