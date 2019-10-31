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
    
    # question 1 : affichage image
    data = np.loadtxt('row_image.dat')
    plot.figure(1)
    plot.subplot(2,2,1)
    plot.imshow(data, vmin = 4000, vmax = 7000)
    plot.title("Image brute")
    plot.colorbar()
    
    # question 2 : choisir deux températures + calculer NUC à deux points
    T1 = np.loadtxt('temp_bb_18C.dat')
    T2 = np.loadtxt('temp_bb_26C.dat')
    
    alpha =  (np.mean(T1)-np.mean(T2))/(T1-T2)
    
    plot.subplot(2,2,2)
    plot.imshow(alpha)
    plot.title("Matrice de gain")
    plot.colorbar()
    
    beta =  np.mean(T1)-alpha*T1
    
    plot.subplot(2,2,3)
    plot.imshow(beta)
    plot.title("Matrice d'offset")
    plot.colorbar()
    
    