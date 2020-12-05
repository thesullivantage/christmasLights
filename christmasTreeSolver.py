# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:36:33 2020

@author: Jack
"""


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rZero = 10.5
rOne = 10.5*3
# add a lil more on the bottom

# Create the mesh in polar coordinates and compute corresponding Z.


height = 100
inch = 10
stepNum = 100 // inch
print(stepNum)

timeNum = 50
NUM = stepNum*timeNum
# Need compounded so that r has enough to make it all the way around
r = np.linspace(rZero, rOne, NUM)
p = np.linspace(0, 2*np.pi, timeNum)
R, P = np.meshgrid(r, p)


# zInc dep on x inch every rotation (inner loop) -- so dep on stepLoop


# per rot: 
step = -69 / stepNum

# per time 
zStep = step/ timeNum

print(zStep)
# num rotations

zInit = 100
# 50 steps (every 2 inches) -- cut off extra .5 lol 
# 1 lap: 50 steps, need 50 laps


x = np.zeros(NUM)
y = np.zeros(NUM)
z = np.zeros(NUM)
z[0]=69


combInd = 0
pathInt = 0
for i in range(stepNum):
    for t in range(1, timeNum):
        combInd += 1
        # print(ind)
        rHere=r[combInd]
        x[combInd] = rHere*np.cos(p[t])
        y[combInd] = rHere*np.sin(p[t])
        
        # go back Z 
        z[combInd] = z[combInd-1] + zStep
        print(z[combInd])
        np.abs(np.sqrt(z[combInd]**2+y[combInd]**2+x[combInd]**2))



intercept = 100.5
# Height
newZ = (intercept)-np.abs(R)*3


# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Eval Path Integral Approximation (forward step using vector subtraction)
x0 = x[5:490]
y0 = y[5:490]
z0 = z[5:490]
path= 0
for p in range(1, len(x0)):
    elm = np.abs(np.sqrt(x0[p]**2+z0[p]**2+z0[p]**2)-np.sqrt(x0[p-1]**2+z0[p-1]**2+z0[p-1]**2))
    print(elm)
    path += elm
    
print("Total inches lights needed: ", path)

# Plot the surface.
# ax.plot_surface(X, Y, newZ, cmap=plt.cm.YlGnBu_r)
ax.plot3D(x0, y0, z0, 'magenta')

# Tweak the limits and add latex math labels.
ax.set_zlim(0, 75)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

plt.show()

# Finding our intercept: 
# (10.5, 69)
# (10, 70.5)
# (0, 100.5)

# X at 33.5