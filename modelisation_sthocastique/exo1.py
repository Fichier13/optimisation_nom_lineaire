import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

"""
randint(1,4) permet de generer un nombre entre 1 et 4
"""
def sumila(x):
    tab=[x]
    while x!=3:
        if x==1:
            x=npr.randint(1,4)
        else:
            x=npr.randint(2,4)
        tab.append(x)
    return tab


def aproximation(N,x):
    Temps=0
    for i in range(N):
        Temps +=len(sumila(x))-1
    return Temps/N
        
def graph_approximation_temps(x,N):
    Temps=0 
    stock=[]
    for i in range(1,N+1):
        Temps +=len(sumila(x))-1
        stock.append(Temps/i)
        
    return stock
        


N=1000
x=1
print (sumila(1))
print (aproximation(1000,1))

plt.plot(np.arange(0,N),graph_approximation_temps(x,N),'b+',label="valeur aproche")
plt.plot(np.arange(0,N),np.ones(N)*2.5,'r',label="valeuyr theorique")
plt.legend()
    