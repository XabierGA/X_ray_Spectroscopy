# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:48:39 2018

@author: xabia
"""

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

energy = [4.59, 8.16, 15.94, 22.10]
sy = [0.09,0.04,0.03,0.05]
z = [21 , 28 , 39 ,46 ]
zsquared = [x**2 for x in z]

def func(x,a,b):
    return a*x+b

fittedParameters, covar = curve_fit(func,zsquared,energy)
print(fittedParameters)
print(covar)

plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k', )

plt.errorbar(zsquared, energy, yerr=sy , xerr=None,fmt='mo',label='Measured', ms = 8) 
x = np.linspace(min(zsquared), max(zsquared), 1000)
a=fittedParameters[0]
b=fittedParameters[1]
tt=func(x,a,b)
plt.plot(x, tt, 'b-', label='Linear Regression') 
plt.title('Moseley Law')
plt.xlabel('$(Z-1)^2$ ')
plt.ylabel('E $kEV$  ')
plt.legend(prop={'size':13})
plt.grid(True)

plt.savefig('moseley_law.pdf')