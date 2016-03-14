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

def moindre_carre(x, y) :
   return np.linalg.inv(x.dot(x.T)).dot(x.dot(y))

def jlabs_mc(x, y, N) :
	return np.sum(np.absolute(p - moindre_carre(x, y).T.dot(x))) / N

def jl2_mc(x, y, N) :
	return np.dot((y - np.dot(x.T,moindre_carre(x, y))).T, (y - np.dot(x.T, moindre_carre(x, y)))) * (1./N)

def jl1_mc(x, y, N) :
	return sqrt(jl2_mc(x, y, N) * N) / N

def jlinf_mc(x, y) :
	return np.max(np.absolute(y - moindre_carre(x, y).T.dot(x)))


#### Prints #####


print "TP1", theta
print "jlabs =", jlabs(x, p, theta, N)
print "jl1 =", jl1(x, p, theta, N)
print "jl2 =", jl2(x, p, theta, N)
print "jlinfini =", jlinf(x, p, theta), "\n"

print "TP2"
mc = moindre_carre(x, p)
print "Moindre Carres", mc
print "jlabs =", jlabs_mc(x, p, N)
print "jl1 =", jl1_mc(x, p, N)
print "jl2 =", jl2_mc(x, p, N)
print "jlinfini =", jlinf_mc(x, p)

#################


#### Graphs #####

## TP1
plt.plot(t, p, 'ro')
plt.plot(range(5, 16), [f(x) for x in range(5, 16)], "g", label="2x+3")
##

## TP2
plt.plot(range(5, 16), [(x * mc[0] + mc[1]) for x in range(5,16)], "b", label="moindre carre")
##

plt.legend()
plt.show()

#################
