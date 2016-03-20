import matplotlib.pyplot as plt
import numpy as np
import sys
from math import sqrt

##### READ ######

x0 = np.loadtxt('x0.txt')
y0 = np.loadtxt('y0.txt')
x1 = np.loadtxt('x1.txt')
y1 = np.loadtxt('y1.txt')
x2 = np.loadtxt('x2.txt')
y2 = np.loadtxt('y2.txt')

x2.sort()
y2.sort()



##### FONCTIONS #####

def moindre_carre(x, y) :
   return np.linalg.inv(x.dot(x.T)).dot(x.dot(y))

def polynome(x, y, puissance):
	res = np.zeros((puissance + 1, len(x)))

	for i in range(0, puissance + 1):
		res[i,:] = np.power(x, puissance - i)

	return res


if (len(sys.argv) == 2):
	res = polynome(x2, y2, int(sys.argv[1]))
else:
	res = polynome(x2, y2, 13)



##### Graphs #####

plt.plot(x2, y2,'ro', label="datas")
plt.plot(x2, np.dot(moindre_carre(res, y2), res), 'g', label="estimation")
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.legend(loc=4)
plt.show()

#################
