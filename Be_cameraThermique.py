# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:27:50 2019

@author: denes
"""
#
#Afficher le contenu d’une matrice sous la forme d’une image
#
#plot.figure(1)
#plot.imshow(data, vmin=25, vmax=35)
#plot.colorbar()
#plot.show()
#Quelques fonctions utiles
#scipy.optimize.curve_fit
#numpy.where

import numpy as np
import matplotlib.pyplot as plot

if __name__ == "__main__" :
    
    
    data = np.loadtxt('row_image.dat')
    plot.figure(1)
    plot.subplot(2,2,1)
    plot.imshow(data)
    