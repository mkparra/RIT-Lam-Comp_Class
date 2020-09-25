# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:02:37 2020

@author: Mike Ortiz
"""
# Here we are doing problem 4 of HW3. Using a damped HMO for our three
# methods, Eular, Huens, RK4

from numpy import linspace, cos, zeros, pi
import matplotlib.pyplot as plt
from Prob_3_HW3 import Eulars, sol, RK4thOrder

w = 2
P = 2*pi/w
dt = P/200
T = 3*P
N_t = int(round(T/dt))
print(N_t)
t = linspace(0, N_t*dt, N_t+1)
print(len(t))

u = zeros(N_t+1)
v = zeros(N_t+1)
print(len(u))
print(len(v))
# Initial condition
A = 2
u[0] = A
v[0] = 0

# Step equations forward in time
def Eulars(u,v):
    for i in range(N_t):
        u[i+1] = u[i] + dt*v[i]
        v[i+1] = v[i] - dt*w**2*u[i]
    return t
t = Eulars(u,v)

plt.plot(t, u, 'b-')
plt.plot(t, A*cos(w*t), 'r')

plt.legend(('numerical', 'exact'))
plt.xlabel('t')
plt.show()
plt.savefig("/Users/Mike Ortiz/Documents/GitHub/RIT-Lam-Comp_Class/HW3/Damp_Eulars.png")

#%%
# for this part we will be using he Huens method 
import numpy as np 
import matplotlib.pyplot as plt
from Prob_3_HW3 import Eulars, Heun, RK4thOrder
w = 2
P = 2*pi/w
dt = P/200
T = 3*P
N_t = int(round(T/dt))
t = linspace(0, N_t*dt, N_t+1)
print(len(t))
u = np.zeros(t.size)
A = 4
u[0] = A
def Damp(t,u):
    return u
def Heun(t,u):
    return A*cos(w*t)
    for i in range(1,t.size):
        u_interm = u[i-1] + N_t*Heun(t[i-1],u[i-1])
        
        u[i] = u[i-1] + (N_t/2)*(Heun(t[i-1],u[i-1])+Heun(t[i],u_interm))
    return t
t = Heun(t,u)
plt.plot(t, u, 'b-')
plt.plot(t, A*cos(w*t), 'r')
plt.legend(('numerical', 'exact'))
plt.xlabel('t')
plt.show()
plt.savefig("/Users/Mike Ortiz/Documents/GitHub/RIT-Lam-Comp_Class/HW3/Damp_Heun.png")



#%%


import numpy as np
from numpy import zeros, linspace
from Prob_3_HW3 import Eulars, Heun, RK4thOrder

w = 2
P = 2*pi/w
dt = P/200
T = 3*P
h = int(round(T/dt))
t = linspace(0, h*dt, h+1)
print(len(t))
u = np.zeros(t.size)
A = 4
u[0] = A
v[0] = 0


def feval(funcName, *args): 
    return eval(funcName)(*args)

def RK4thOrder(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0])/h)
    
    x = x_range[0]
    y = yinit
    
    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        k1 = feval(func, x, y)
        yp2 = y + k1*(h/2)
        k2 = feval(func, x+h/2, yp2)
        yp3 = y + k2*(h/2)
        k3 = feval(func, x+h/2, yp3)
        yp4 = y + k3*h
        k4 = feval(func, x+h, yp4)

        for j in range(m):
            y[j] = y[j] + (h/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])
        x = x + h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])  
    return [xsol, ysol]












 
