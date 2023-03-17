# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:33:35 2022

@author: cgsan
"""

# Cole Sanders
# 12/1/22
# Approximates the position of every point along a hanging chain fixed between two points

import numpy as np
import matplotlib.pyplot as plt

# Number of sections the chain is split up into for calulations
N = 100

# Constant for force equation on each section of the chain
k = 5.0

# (x0, y0) and (x1, y1) represent the location of the fixed ends of the chain in the x,y plane
y0 = 0
y1 = 2
x0 = 0
x1 = 1

# Number of relaxations preformed initally set to zero
sweeps = 0

# Create a 2D grid of space the chain occupies
X = np.linspace(x0,x1,N+1)
y = np.linspace(y0,y1,N+1)

# the inital estimation of the chain hanging in a perfectly straight line between the two points
for i in range(0,len(y)):
    y[i] = 2*X[i]

# Sets the threshold for minimum change from one approximation to another to signal the end of the process
lmax = 0.000000001

# Calvulates the width of one square in the 2D grid
h = X[1] - X[0]

# Variable initialized to hold a plot of the chain's approximation before the most recent (used for error calculation)
yold = np.linspace(y0,x1,N+1)

# L is a variable representing a numerical value of the degree of difference between the previous approximation
# (yold) to the current one (y)
L = 100

# Keep preforming relaxations/approximations until the differences between them are less than the threshold value
while(L > lmax):
    # Increase the number of approximations to get the plot by 1000
    sweeps += 10000
    # Apply force equation to approximate a more accurate position of each segment along the chain
    for x in range(0, sweeps):
        y[1:-1] = .5 * (y[:-2] + y[2:]) - ((k*(h**2))/2)*np.sqrt(1 + (y[:-2] - y[2:])**2/((2*h)**2))
    
    # Calculate magnitude of difference between the new approximation and the previous one.
    L = (1/N)*sum(np.abs(y[1:-1]-yold[1:-1]))
    m = y-yold
    
    # Set the new approximation to be the previous approximation
    for x in range(1, len(y)):
        yold[x] = y[x]
    
        
# Plots a graph of the chains location
plt.close()
plt.plot(X,y,"r") 
plt.title("Y vs X of a hanging chain")
plt.xlabel("x") 
plt.ylabel("y") 
plt.show()