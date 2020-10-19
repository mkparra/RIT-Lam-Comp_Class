# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:24:52 2020

@author: Mike Ortiz
"""
# For problem 1 we need to use the linear least squares method to be able 
# to estimate some variables from equation 3 in the HW. We are given freedom 
# to choose what ever photometric band we want. I think I will choose Vmag 
# since it is more known.

import numpy as np
import pandas as pd 
from numpy import log10, transpose, matmul
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as m3d

# Funtion to calculate Abs Mag's for differnt bands with the numbers from the HW table
def Abs_Mag(d,m_lam,Ex,m_band):
    if m_band == "J":
        A_lam = .271*3.1*Ex
    elif m_band == "H":
        A_lam = .175*3.1*Ex
    elif m_band == "K":
        A_lam =.117*3.1*Ex
    else:
        A_lam = 3.1*Ex
    return  -(5*log10(d*10**3))+5+m_lam-A_lam   


# Function to calculate Abs Mag from relation of the box equation in HW
def M_relation(logP,logZ,p):
    alpha = p[0]
    beta = p[1]
    gamma = p[2]
    return alpha+(beta*logP)+(gamma*logZ)

# Function to calcualte the least square fit from notes from class
def Least_Sqr(mat,M,sigma):

    AT = transpose(mat)
    ATA = matmul(AT,mat)
    ATAinv = np.linalg.inv(ATA)
    ATAinvAT = matmul(ATAinv,AT)
    coeffs = matmul(ATAinvAT,M)
    errors = [[sigma*np.sqrt(ATAinv[i][i]) for i in range(len(ATAinv))]]
    return coeffs,errors

        
# #importing the data from the HW and only selection period, mag, metalicity
data = pd.read_csv("cepheid_data.txt",usecols=[1,2,3,4,5,6,7,8],names=['Period(days)','d','V(mag)','J(mag)','H(mag)','K(mag)','Ex','logZ'],skiprows=1,dtype=float)

#print(data["Period(days)"])
#print(data["V(mag)"])


# Turning our data of P into an array to use np against
logP = np.array(log10(data['Period(days)'].values))
# Same thing here in turning our mags into an array to use
logZ = np.array(data['logZ'].values)

# #  print(logP)
# # print(logZ.dtype)

# Calling the function Abs Mag to our data
M = Abs_Mag(data['d'],data['V(mag)'],data['Ex'],'V')
# Changing M from series to numpy array
M = M.values
# Creating our design matrix 
mat = np.c_[np.ones(len(logP)),logP,logZ]

# print(type(mat))
# Calling our Least_Sqr function 
p,e = Least_Sqr(mat,M,0.1)

# print(p)

# Calling our M_realation function
M_pred = M_relation(logP,logZ,p)

# # print(len(mat))
print(p)
print(e)

# HEre we are plotting both plots of period and metallicity
fig,ax = plt.subplots(1,2)
ax[0].scatter(logP,M)
ax[0].scatter(logP,M_pred)
ax[0].set_xlabel('Log of Period(in Days))')
ax[0].set_ylabel('apparent magnitude')

ax[1].scatter(logZ,M)
ax[1].scatter(logZ,M_pred)
ax[1].set_xlabel('Log of Metallicity')
ax[1].set_ylabel('apparent magnitude')
fig.suptitle('V-band magnitudes')

