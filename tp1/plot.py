import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

##### READ ######

p = np.loadtxt('p.txt')
t = np.loadtxt('t.txt')

#################


### VARIABLES ###

def f(x):
    return 2*x + 3

theta = np.array([2, 3])
N = 100.
x = np.array([np.array([i, 1]) for i in t]).T

alpha = 0.001
MAX_IT = 1000

#################

def jlabs(x, y, theta, N) :
	return np.sum(np.absolute(y - theta.T.dot(x))) / N

def jl2(x, y, theta, N) :
	return np.dot((y - np.dot(x.T,theta)).T, (y - np.dot(x.T, theta))) * (1./N)

def jl1(x, y, theta, N) :
	return sqrt(jl2(x, y, theta, N) * N) / N

def jlinf(x, y, theta) :
	return np.max(np.absolute(y - theta.T.dot(x)))


#### Prints #####

print "TP1\ntheta =", theta
print "jlabs =", jlabs(x, p, theta, N)
print "jl1 =", jl1(x, p, theta, N)
print "jl2 =", jl2(x, p, theta, N)
print "jlinfini =", jlinf(x, p, theta)

#################


#### Graphs #####

plt.plot(t, p, 'ro')
plt.plot(range(5, 16), [f(x) for x in range(5, 16)], "g", label="2x+3")

plt.legend()
plt.show()

#################
