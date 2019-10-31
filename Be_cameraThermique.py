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
from scipy import optimize

def planck(DL, R, B, O):
        return B / np.log(R / (DL - O) + 1)

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
    
    #print("Pixels defectueux")
    #print(calib)
    
    # 4 : Planck 
    
    DL = []
    for temp in range (16, 44, 2):
        file = 'temp_bb_{}C.dat'.format(temp)
        data_all = np.loadtxt(file)
        #print(data)
        #print(alpha.min(), alpha.max(), beta.min(), beta.max())
        nuc_data = alpha*data_all + beta
        #(nuc_data)
        gamma = np.sum(nuc_data*calib)
        gamma /= np.sum(calib)
        
        DL.append(gamma)
    
    #print(DL)
    
    ydata = np.arange(16,44,2)+ 273.15  
    xdata = DL
    
    plot.figure(3)
    
    plot.plot(xdata,ydata,'-*')
    plot.xlabel("DL")
    plot.ylabel("T en °K")
    
    p0 = np.array([5e7, 1e3, 1e3])
    bounds = (0, np.inf)
    
    R, B = optimize.curve_fit(planck, xdata, ydata, p0=p0, bounds=bounds)
    plot.plot(xdata, planck(xdata, *R))
    print(R)
    
    #5 : 
    
    #exemple prof 
    image = planck(nuc_data, *R)
    image -= 273.15
    plot.figure(4)
    plot.imshow(image, vmin=39.9, vmax=40.1)
    plot.colorbar()
    
    image = planck(NUC, *R)
    image -= 273.15
    plot.figure(5)
    plot.imshow(image, vmin=27, vmax=35)
    plot.colorbar()
    