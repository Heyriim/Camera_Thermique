# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:27:50 2019

@author: denes
"""

import numpy
import matplotlib.pyplot as plot
data = np.loadtxt(’fichier.txt’)
Afficher le contenu d’une matrice sous la forme d’une image

plot.figure(1)
plot.imshow(data, vmin=25, vmax=35)
plot.colorbar()
plot.show()
Quelques fonctions utiles
scipy.optimize.curve_fit
numpy.where
