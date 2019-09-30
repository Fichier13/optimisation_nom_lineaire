import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

"""
si U suit une lois une loi uniforme u([0,1])

"""
def sumila_marche(x,N,p):
      tab=[x]
      
      for i in range(N):
          saut=2*(npr.rand(1)<p)-1
          x += saut
          tab +=[x]
      return tab
  



v=sumila_marche(x,N,p)
w=[x]+v
x=0
N=100
p=[1/4,1/2,3/4]
abs=np.arange(0,N+1)

for i in range(3):
    plt.step(abs,sumila_marche(x,N,p),label=p[i])
    plt.plot(abs,abs*(2*p[i]-1),'---',label)
    plt.legend()


