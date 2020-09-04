#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:15:48 2020

@author: mikeortiz-parra
"""
# Problem 5, write a linear interpolation with a set of given x and y points.
# This should return a funtion that should be able to use to interpolate new y values


def inter(x_0,y_0,x_1,y_1): #creating a generalized function to be used in prob 6 with the data will be getting 
    slope = (y_1-y_0)/(x_1-x_0) # Using basic slope for a line since asking for linear interpolation
    def f(x):
        return (slope*(x-x_0)+y_0)
    return f