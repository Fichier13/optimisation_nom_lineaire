import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from random import randrange, uniform


from scipy.optimize import minimize
global sources, ePercentages




def priceFunction(x,y):
    res=x**2-y*x
    return res
   
   
def function2(x):
    return x**2



 
res = minimize(priceFunction, 10, args=(5),
               method='nelder-mead',
               options={'xtol': 1e-7, 'disp': True})
print("la methode nelder-mead produit le point", res.x)
print('la valeur pour ce point est', priceFunction(res.x, 5))
print(' ')


res = minimize(function2, 10,
               method='nelder-mead',
               options={'xtol': 1e-7, 'disp': True})
print("la methode nelder-mead produit le point", res.x)
print('la valeur pour ce point est', function2(res.x), res.fun)
print(' ')



