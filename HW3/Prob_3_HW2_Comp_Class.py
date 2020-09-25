#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:23:35 2020

@author: mikeortiz-parra
"""
# Problem 3 will be creating a class for matrix. We will be able to call this 
# in the next homework set to do acually calculations. The class will be able 
# to do lots of things like add multiple and transpose etc etc
#
import numpy as np


class Matrix:
    # The init here is making our matrix to use for the rest of the fuctions
    def __init__(self,dims,fill=True,arr=None):
        self.rows = dims[0]
        self.cols = dims[1]
        
        
        # self.g=dims
        if fill: # If statment for filled Matrix to match rows and cols
            self.m = [[0]*self.cols for i in range (self.rows)]
        elif self.rows*self.cols == len(arr):
            self.m = [[0]*self.cols for i in range (self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    self.m[i][j] = arr[(3*i)+j]
        else:
            print("error")   
    
        

            
                
    def __add__(self,other):
        m=[[0 for i in range(self.cols)]for j in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                 self.g[i][j] + other.g[i][j]
        
        return(m)
        
    def __mul__(self,other):
        if self.cols == other.rows:
            C = Matrix([self.rows,other.cols])
            for i in range(self.rows):
                for j in range (other.cols):
                    s = 0
                    for n in range(self.cols):
                        s = s+(self.m[i][n]*other.m[n][j])
                    C.m[i][j] = s
            return C
        else:
            print("Error")
    # Making a transpose matrix here and setting a matrix minor to be able to 
    # take away a row and add a row to make the transpose work
    def transpose(self):
        T = Matrix([self.cols,self.rows])
        for j in range(self.rows):
            for i in range(self.cols):
                T.m[i][j] = self.m[j][i]
        return T
    
    def MatrixMinor(self,i,j):
        C = Matrix([self.rows-1,self.cols-1])
        C.m = [row[:j] + row[j+1:] for row in (self.m[:i]+self.m[i+1:])]
        return C
    
    def MatrixDeter(self):
        #base case for 2x2 matrix
        if len(self.m) == 2:
            return self.m[0][0]*self.m[1][1]-self.m[0][1]*self.m[1][0]
    
        determinant = 0
        for c in range(len(self.m)):
            determinant += ((-1)**c)*self.m[0][c]*self.MatrixMinor(0,c).MatrixDeter()
        return determinant
    
    def trace(self):
        val = 0
        if self.row == self.column:
            for i in range(self.row):
                val = val+self.m[i][i]
        else:
            print('The Trace does not exist')
        return(val)
 # Here we are taking the invers and using the Determinate as to matrix math 
 # to find the inverse and using cofactors to build a 2x2 inside a 3x3 to make
 # sure the inverse happens with if and else/if and else staments to make sure 
 # the right numbers are being inversed. Cannot equal rows and cols: per if statment
    def inverse(self):
        if self.rows != self.cols:
            print("Inverse does not exist")
        elif self.MatrixDeter() == 0:
            print("Inverse does not exist")
        else:
            det = self.MatrixDeter()
            if self.rows == 2:
                C = Matrix([2,2])
                C.m = [[self.m[1][1]/det, -1*self.m[0][1]/det],[-1*self.m[1][0]/det, self.m[0][0]/det]]
                return C
            cofactors = []
            for r in range(self.rows):
                cofactorRow = []
                for c in range(self.cols):
                    minor = self.MatrixMinor(r,c)
                    cofactorRow.append(((-1)**(r+c)) * minor.MatrixDeter())
                cofactors.append(cofactorRow)
            cof_mat = Matrix([len(cofactors),len(cofactors)])
            cof_mat.m = cofactors
            cofactors = cof_mat
            cofactors = cofactors.transpose()
            for r in range(cofactors.rows):
                for c in range(cofactors.cols):
                    cofactors.m[r][c] = cofactors.m[r][c]/det
            return cofactors
# LU we are building the corners of the matrix and plugging in val = 0 to 
# make sure after all the if statments to allow a the zero corners and 1 diagnaly
# Note I didnt get exactly zero for two mubers but was really really small like 
# e-17 small
    def LU(self):
        
        if self.rows != self.cols:
            print("Error: Cannot decompose. Enter square matrix.")
        else:
            lower = Matrix([self.rows,self.rows])
            upper = Matrix([self.rows,self.rows])
            for i in range(self.rows):
                for j in range(self.rows):
                    if j<i:
                        pass
                    elif i == j:
                        lower.m[j][j] = 1
                        
                        val = 0
                        for k in range(i):
                            val = val+(lower.m[i][k]*upper.m[k][i])
                        upper.m[i][j] = self.m[j][i]-val
                    else:
                        val = 0
                        for k in range(i):
                            val = val + (lower.m[j][k]*upper.m[k][i])
                        lower.m[j][i] = (self.m[j][i]-val)/upper.m[i][i]
                        
                        val = 0
                        for k in range(i):
                            val = val + (lower.m[i][k]*upper.m[k][j])
                        upper.m[i][j] = self.m[i][j] - val
        return(lower,upper)
    # I found out how to pring matrices to make it more readable and to see what 
    # is going on number wise.
    def mat_print(self):
        mat = ''
        for each in range(self.rows):
            mat = mat+str(self.m[each][:])+'\n'
        return mat
        

# A = Matrix([3,3],fill=False,arr=[1,2,3,4,5,6,-7,8,9])
# # B = Matrix([2,3],2)
# # print(A.inverse().m)
# print(A.mat_print())
# # print(B.m)
# # print(B.m)
# # D = A*B
# # print(C.m)
# #print(A.transpose().m)
# # print(D.m)
# print(A.MatrixDeter())
# l,u = A.LU()
# inv = A.inverse()
# I  = A*inv
# print(inv.mat_print())
# print(I.mat_print())
# print(l.mat_print())
# print(u.mat_print())
# a=[[1,2,3],[10,23,25],[14,17,18]]
# b=[[1,9,10],[6,2,8],[2,4,3]]
# m1=Matrix(a)
# m2=Matrix(b)
# b=m1.__add__(m2)
# #%%
#         if fill: # If statment for filled Matrix to match rows and cols
#             self.m = [[0]*self.cols for i in range (self.rows)]
#         elif self.rows*self.cols == len(arr):
#             self.m = [[0]*self.cols for i in range (self.rows)]
#             for i in range(self.rows):
#                 for j in range(self.cols):
#                     self.m[i][j] = arr[(3*i)+j]
#         else:
#             print("error")   