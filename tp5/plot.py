import numpy as np
import matplotlib.pyplot as plt
from math import exp


f = np.loadtxt("taillepoids_f.txt")
h = np.loadtxt("taillepoids_h.txt")

print f

def sigmoid(x):
    return (1. / 1. + exp(-x))

def regressLog(x, y, theta, N):
    return np.sum(np.dot(x, y - sigmoid(np.dot(theta.T, x)))) * (-1./N)


plt.plot(h, "r.")
# plt.show()
