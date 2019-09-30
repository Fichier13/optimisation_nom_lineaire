import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

def riune(x,N,p) :
    z=x
    stoks=[x]
    while z!=0 and z!=N:
        z+=2*(npr.rand()<p)-1
        stoks.append(z)
        return stoks
    
    
    

N=100
x=1
p=1/2

print(riune(x,N,p))

for i in range(3):
    v=riune(x,N,p)
    n=len(v)
    plt.step(np.arange(n),v)