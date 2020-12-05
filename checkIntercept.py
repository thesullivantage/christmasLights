# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:21:18 2020

@author: Jack
"""
import matplotlib.pyplot as plt
import numpy as np 

x = [0, 1, 2]
y = np.abs(x)*3


print()
print(np.arctan2(6, 2)*(180/(np.pi)))

x = np.linspace(0, 10.5*3, 2500)

y = 100.5-np.abs(x)*3

# checks
print(y[1]-y[0])
print(y[1])
    
    


plt.xlabel('x'); plt.ylabel('cos(x)')
plt.axis([0,100, 0, 105])
plt.plot(x, y, '-', label='test')
plt.show()

