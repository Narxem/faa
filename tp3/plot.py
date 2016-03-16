import matplotlib.pyplot as plt
import numpy as np
import math

##### READ ######

p = np.loadtxt('p.txt')
t = np.loadtxt('t.txt')

#################


### VARIABLES ###

def f(x):
    return 2 * x + 3

x = np.array([np.array([i, 1]) for i in t]).T
N = 100.
#################


def jlabs(x, y, theta, N) :
	return np.sum(np.absolute(y - theta.T.dot(x))) / N

def jl2(x, y, theta, N) :
	return np.dot((y - np.dot(x.T,theta)).T, (y - np.dot(x.T, theta))) * (1./N)

def jl1(x, y, theta, N) :
	return math.sqrt(jl2(x, y, theta, N) * N) / N

def jlinf(x, y, theta) :
	return np.max(np.absolute(y - theta.T.dot(x)))

def alpha(t) :
    return 1. / (1. + 4000. * float(t))

def descenteGradient(x, y, t, theta, epsilon = 0.00000001, N = 100) :
	temps = t
	ancien_theta = theta
	tab = [ancien_theta]
	while(True) :
		gradiant = np.dot(x,(y - np.dot(x.T, ancien_theta)))
		nouveau_theta = ancien_theta + np.dot(np.dot(alpha(t), gradiant), 1. / float(N))

		if math.fabs(jl2(x, y, nouveau_theta, N)-jl2(x, y, ancien_theta, N)) <= epsilon :
			return tab
		else :
			ancien_theta = nouveau_theta
			tab.append(ancien_theta)
			temps += 1

#### Prints #####

DG = descenteGradient(x, p, 1, [10., 3.]) 

print "Descente de gradient : ", DG[-1]


print "TP3 - Mesures de performance"
print "jlabs =", jlabs(x, p, DG[-1], N)
print "jl1 =", jl1(x, p, DG[-1], N)
print "jl2 =", jl2(x, p, DG[-1], N)
print "jlinfini =", jlinf(x, p, DG[-1])
#################


#### Graphs #####

plt.plot(range(0, len(DG)), [DG[i][0] for i in range(0, len(DG))], "r")
plt.plot(range(0, len(DG)), [DG[i][1] for i in range(0, len(DG))], "g")

plt.legend()
plt.show()

#################

"""
descenteGradientStochastique manquante
"""
