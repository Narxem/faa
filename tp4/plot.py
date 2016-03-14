import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

##### READ ######

x0 = np.loadtxt('x0.txt')
y0 = np.loadtxt('y0.txt')
x1 = np.loadtxt('x1.txt')
y1 = np.loadtxt('y1.txt')
x2 = np.loadtxt('x2.txt')
y2 = np.loadtxt('y2.txt')


### FONCTIONS ###

def phi(m, x):
    return np.power(x, m)

def moindre_carre(x, y) :
   return np.linalg.inv(x.dot(x.T)).dot(x.dot(y))


### VARIABLES ###

m = 20
phiX = np.array([phi(mi, x0) for mi in range(0, m)])
theta = moindre_carre(phiX, y0)


#################


plt.plot(x0, y0, "r.")
plt.plot(x0, [np.array([theta[i] * x0[j]**i for i in range (0, m)]) for j in range(0, 100)])
plt.show();
