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

def planck(R,B,T) :
    return
if __name__ == "__main__" :
    
    # 1 : affichage image
    
    data = np.loadtxt('row_image.dat')
    plot.figure(1)
    plot.imshow(data, vmin = 4000, vmax = 7000)
    plot.colorbar()
    plot.figure(2)
    plot.subplot(2,2,1)
    plot.imshow(data, vmin = 4000, vmax = 7000)
    plot.title("Image brute")
    plot.colorbar()
    
    # 2 : choisir deux températures + calculer NUC à deux points
    
    T1 = np.loadtxt('temp_bb_18C.dat')
    T2 = np.loadtxt('temp_bb_26C.dat')
    
    alpha =  (np.mean(T1)-np.mean(T2))/(T1-T2)
    
    plot.subplot(2,2,2)
    plot.imshow(alpha,vmin = 0.75,vmax = 1.25)
    plot.title("Matrice de gain")
    plot.colorbar()
    
    beta =  np.mean(T1)-alpha*T1
    
    plot.subplot(2,2,3)
    plot.imshow(beta, vmin =-300,vmax = 200)   #
    plot.title("Matrice d'offset")
    plot.colorbar()
    
    NUC = alpha * data + beta
    plot.subplot(224)
    plot.imshow(NUC, vmin=4000, vmax=7000)
    plot.title("NUC")
    plot.colorbar()
    
    # 3 : mettre en place un algorithme de détection de pixels défectueux
    
    #bruit_rms = np.sqrt(1)
     
    calib = np.where((alpha < 0.75) | (alpha > 1.25) | (beta < -5000) | (beta > 5000),0,1)  
    alpha[np.where((alpha < 0.75) | (alpha > 1.25) | (beta < -5000) | (beta > 5000))] = 1.
    beta[np.where((alpha < 0.75) | (alpha > 1.25) | (beta < -5000) | (beta > 5000))] = 0.
    print("Pixels defectueux")
    print(calib)
    
    # 4 : Planck 
    
    DL = []
    TBB = []
    for temp in range (16, 42, 2):
        file = 'temp_bb_{}C.dat'.format(temp)
        data = np.loadtxt(file)
        print(data)
        print(alpha.min(), alpha.max(), beta.min(), beta.max())
        nuc_data = alpha*data + beta
        print(nuc_data)
        gamma = np.sum(nuc_data*calib)
        gamma /= np.sum(calib)
        
        DL.append(gamma)
    
    print(DL)
        
    
    