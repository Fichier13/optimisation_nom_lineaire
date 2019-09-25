#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:43:10 2019

@author: niang
"""
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(8,8))
fig, ax = plt.subplots(1)


N=150
T=[]
def cercle(a,b,R):
    for k in range(N+1):
        T.append(2*np.pi*k/N)
    xpoints=R*np.cos(T)+a
    ypoints=R*np.sin(T)+b
    ax.plot(xpoints,ypoints,color='green')
    ax.set_aspect(1)



        
    
    

    
    

cercle(1,2,2)
cercle(2,3,1)
cercle(3,4,5)





