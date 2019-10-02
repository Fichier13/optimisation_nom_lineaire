from scipy import misc

import matplotlib.pyplot as plt
import numpy as np


def fonction(x):
    y=np.cos(x)*np.exp(-(x-np.pi)**2)
    return y





def descent(fonction,alpha,x0,eps):
    cond=100
    nb_iteration=0
    y0=fonction(x0)
    plt.scatter(x0,y0)
    while cond>eps and nb_iteration<100:
        x0=x0-alpha*misc.derivative(fonction,x0)
        y0=fonction(x0)
        nb_iteration=nb_iteration+1
        plt.scatter(x0,y0)
    plt.title("descente du gradiant")
    plt.grid()
    
    
x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = fonction(x)

plt.plot(x, y,'b-')

descent(fonction,0.8,2.1,0.0001)


    