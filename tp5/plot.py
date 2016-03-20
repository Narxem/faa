import numpy as np
import matplotlib.pyplot as plt
import math
import random

##### READ ######

def read(pathname) :
	fichier = open(pathname, 'r')
	(taille, poids) = ([], [])
	for line in fichier :
		(ligne_taille, ligne_poids) = line.split()
		taille.append(float(ligne_taille))
		poids.append(float(ligne_poids))
	return (taille, poids)

(tmp_taille_f, tmp_poids_f) = read('taillepoids_f.txt')
(tmp_taille_h, tmp_poids_h) = read('taillepoids_h.txt')

### VARIABLES ###

taille_f = np.array(tmp_taille_f, float)
taille_h = np.array(tmp_taille_h, float)

poids_f = np.array(tmp_poids_f, float)
poids_h = np.array(tmp_poids_h, float)

nbFilles = len(taille_f)
nbHommes = len(taille_h)

#################

def sigmoid(x):
	return 1. / (1. + math.exp(-x))

def sigmoidVecteur(vecteur) :
	newVecteur = np.copy(vecteur)
	for i in range(len(vecteur)) :
		newVecteur[i] = sigmoid(vecteur[i])
	return newVecteur

def risqueEmpirique(x, y, theta, N):
	sigmo = sigmoidVecteur(np.dot(x.T, theta))
	interm = np.dot(-y, np.log(sigmo)) - np.dot((1 - y), np.log(1 - sigmo))
	return np.sum(interm) / float(N)

def alpha(t) :
	return 1. / (1. + 4000. * float(t))

def descenteGradientSigmoide(x, y, t, theta, epsilon = 0.00000001, N = 100) :
	temps = t
	ancien_theta = theta
	while(True) :
		gradiant = np.dot(x,(y - sigmoidVecteur(np.dot(x.T,ancien_theta))))
		nouveau_theta = ancien_theta + np.dot(np.dot(alpha(t), gradiant), 1. / float(N))

		if risqueEmpirique(x, y, ancien_theta,N) - risqueEmpirique(x, y, nouveau_theta, N) <= epsilon :
			return ancien_theta
		else :
			ancien_theta = nouveau_theta
			temps += 1

def descenteMultiple(x, y, n, t, epsilon, N) :
	res = []
	listeTheta = []

	for i in range(n) :
		listeTheta.append(np.array([random.random(), random.random()], float))

	for theta in listeTheta :
		res.append(descenteGradientSigmoide(x, y, t, theta, epsilon, N))

	return res

#### Main #####

classe0 = np.zeros(nbFilles)
classe1 = np.ones(nbHommes)

probUnSachantX = float(nbHommes / (nbHommes + nbFilles))

matrix = np.ones((2,(nbHommes + nbFilles)))
matrix[1, :] = np.concatenate([taille_f, taille_h])
lesClasses = np.concatenate([classe0,classe1])

lesThetasLearn = descenteMultiple(matrix, lesClasses, 10, 1, 0.000001, len(lesClasses))
seuil = 0.6

#### Graphs #####

plt.ylim(-1,2)
plt.plot(taille_h, classe1, 'bo')
plt.plot(taille_f, classe0, 'ro')
for thetaL in lesThetasLearn :
	A = thetaL[1]
	b = thetaL[0]
	X = (1 / A * math.log(1 - seuil) - math.log(seuil) + b)
	plt.axvline(X)

plt.show()

#################

"""
Changer les noms de fonction si necessaire et possible
Changer les noms de var
Changer la maniere de plot
Changer lecture si possible
"""