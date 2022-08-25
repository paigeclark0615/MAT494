# -*- coding: utf-8 -*-
"""Hmwk1.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ciAGzv3wjUr9SFkZG3u8r1WiPHyrj3P3

HOMEWORK 1.2
"""

#Linear Combinations
#Determine whether the first vector is a linear combination of the other vectors
#(10,5,17);(1,1,3), (1,3,1), (3,2,4)

import numpy as np

A = np.array([[1, 1, 3], [1, 3, 1], [3, 2, 4]])
B = np.array([10, 5, 17])
X = np.linalg.inv(A).dot(B)
print(X)

#Therefore, (10,5,17) is a linear combination of (1,1,3),(1,3,1),(3,2,4)

#Orthogonality
#Find the orthogonal matrix to A=([3 2 6], [1 1 0], [2 2 1])

import numpy as np
A = np.array([[3,2,6],
              [1,1,0],
              [2,2,1]])
Ainv = inv(A)
print("Ainv=")
print(Ainv)

D=A.dot(Ainv)
print("A*Ainv=")
print(D)

#Therefore, Ainv is orthogonal to A

#Eigenvalues and Eigenvectors
#Determine the eigenvalues and eigenvectors for A=([0 2], [2 3])
from numpy.linalg import eig
a = np.array([[0, 2], 
              [2, 3]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)