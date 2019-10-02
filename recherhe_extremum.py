import matplotlib.pyplot as plt
import numpy as np

def function(x):
    y=x**3-3*x**2+2*x+5
    return y

def extremum(a,b,N):
    min=function(a)
    max=function(a)
    p=(b-a)/N
    x=a
    for i in range(1,N):
        x=x+p
        y=function(x)
       
        if y>max:
            max=y
        if y<min:
            min=y
    plt.scatter(x,min)
    plt.scatter(x,max)
    
    print(min)
    print(max)
    plt.title("extremum d'une fonction")
    plt.grid()
            
x = np.arange(-10,10, 0.01)
y = function(x) 

plt.plot(x, y,'b-')

extremum(1,5,10)

