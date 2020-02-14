# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:22:59 2020

@author: w15psnnw
"""

# Perceptron Algorithm
# Linear Classification with Offset

import numpy as np

# Create a random dataset (4x observations, 3x variables)

x = np.random.random([4,3])
y = np.array([1, 0, 1, 1])

# Set number of epochs
T = 1

def perceptron(x, y, T):
    
    # Initilize parameter vectors
    # shape is the number of columns (or variables in x matrix)
    theta = np.zeros(x.shape[1])
    
    # Theta_0 is a scalar
    theta_0 = 0
    
    for t in range(T):
        
        # Loop 
        for i in range(x.shape[0]):
            print(i, theta, theta_0)
            if np.dot(y[i], (np.dot(theta.T, x[i,]) + theta_0)) <= 0:
                theta += np.dot(y[i], x[i])
                theta_0 += y[i]
                
    return theta, theta_0
                
            
    