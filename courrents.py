import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from random import randrange, uniform
# randrange(a,b) gives a random integral value in between a and b
# uniform(a,b) gives a random floating-point value

from scipy.optimize import minimize



global sources, ePercentages

'''
$sources$ sont les sources aquoustiques qui emettent des signaux vers un
recepteur.
$ePercentages$ donne, pour chaque source, le pourcentage qui permet de
calculer l'erreur maximal en fonction de la distance mesuree.

Les points dans le plan seront declares comme des arrays avec 
deux positions.  Voir les sources plus bas.
'''

sources = [np.array([0.,0.]), np.array([10.,0.]), np.array([3.,8.])]
ePercentages = [.1, .15, .1]



def priceFunction(point, distances):
    '''
    La fonction cout qui doit etre optimisee.  $point$ est la position
    du recepteur et $distances$ la liste des distances mesurees aux
    sources acoustiques.
    '''
    y = 0.
    for i in range(len(distances)):
        a = (np.linalg.norm(point-sources[i])-distances[i])**2
        b = 2*ePercentages[i]*distances[i]
        y = y+a/b
    return y
### end of priceFunction      


def dataCreation(point):
    '''
    Produits des distances entachees d'erruers controlees par 
    la liste $ePercentages$.  Les erreurs sont introduites a 
    travers l'utilisation de $uniform$.
    '''
    L = []
    for i in range(len(sources)):
        d = np.linalg.norm(point-sources[i])
        e = d*ePercentages[i]
        L.append(uniform(d-e, d+e))
    return L
### end of dataCreation


def naiveOptimization(x_ini, x_end, y_ini, y_end, distances, nbP_contour):
    '''
    $point$ is the initial position of the receiver.
    Determine the coordinates of the point using naive optimization.
    '''
    # definition de la fonction a utiliser dependant seulement du point
    def f(p): return priceFunction(p, distances)
    
    # creation of the grid serving for the level curves and the
    # search for the optimal point (global minimum!)
    x = np.linspace(x_ini, x_end, nbP_contour)
    y = np.linspace(y_ini, y_end, nbP_contour)
    X, Y = np.meshgrid(x, y)
    Z = [[f(np.matrix([X[i,j],Y[i,j]])) for j in range(nbP_contour)]
         for i in range(nbP_contour)]
    Z = np.array(Z)
    ij = np.unravel_index(Z.argmin(), Z.shape)
    p_min = np.array([X[ij],Y[ij]])
    print('minimal value', f(p_min))

    return p_min
# end of naiveOptimization


def plotProblem(point, x_ini, x_end, y_ini, y_end, nbOfLevels,
                distances, figure, axes):
    '''
    $point$ est la position initiale du recepteur
    $p_min$ est la solution determinee par la methode nelder-mead
    $figure$ est l'espace graphique utilise pour le dessin
    $axes$ est le systeme dans lequel le dessin sera realise

    Le dessin represente les sources acoustiques, la position correcte du
    recepteur, la position calculee et les courbes de niveau de la 
    fonciton $price$.
    '''
    def f(p): return priceFunction(p, distances)
    
    nbPoints = 150
    # creation of the grid serving for the level curves and the
    # search for the optimal point (global minimum!)
    x = np.linspace(x_ini, x_end, nbPoints)
    y = np.linspace(y_ini, y_end, nbPoints)
    X, Y = np.meshgrid(x, y)
    Z = [[f(np.array([X[i,j],Y[i,j]])) for j in range(nbPoints)]
         for i in range(nbPoints)]
    Z = np.array(Z)
    ij = np.unravel_index(Z.argmin(), Z.shape)
    p_min = np.array([X[ij],Y[ij]])
    error = np.linalg.norm(point-p_min)

    # dimensions de l'image
    axes.set_xlim(x_ini-1, x_end+1)
    axes.set_ylim(y_ini-1, y_end+1)
    
    # level curves
    cs = axes.contour(X, Y, Z, nbOfLevels, cmap=mpl.cm.nipy_spectral)
    figure.colorbar(cs, ax=axes)

    axes.contour(X, Y, Z, levels=[f(point)], colors='cyan')
    
    # point and p_min
    axes.scatter(p_min[0],p_min[1], color='red', s=10,\
                label='position optimale')
    axes.scatter(point[0],point[1], color='cyan', s=20,\
                label='position de recepteur')
    axes.scatter([sources[i][0] for i in range(3)],\
                [sources[i][1] for i in range(3)], color='black', s=10,\
                label='sources')

    # the circles
    for k in range(3):
        plotCircle(sources[k], (1+ePercentages[k])*distances[k],
                   nbPoints, 'magenta', figure, axes)
    
    axes.legend()
    return p_min, error
# end of plotProblem


def plotCircle(center, radius, nbOfPoints, color, figure, axes):
    '''
    $center$ is an array defining a point in the plane
    '''
    T = np.linspace(0, 2*np.pi, nbOfPoints + 1)
    X = radius*np.cos(T) + center[0]
    Y = radius*np.sin(T) + center[1]
    axes.plot(X, Y, color=color)
# end of plotCircle

######################################################################
### Tests
######################################################################

# print('\nPremier test\n')
# dists = [6.34, 5.23, 5.72]

# # En utilisant l'algorithme nelder-mead :
# p = np.array([1.2, 6]) 
# res = minimize(priceFunction, p, args=(dists),
#                method='nelder-mead',
#                options={'xtol': 1e-7, 'disp': True})
# print("la methode nelder-mead produit le point", res.x)
# print('la valeur pour ce point est', priceFunction(res.x, dists))
# print(' ')
# print("l'optimisation naive produit le point",
#       naiveOptimization(3., 6., 1., 5., dists, 200), "\n\n")


######################################################################
print('\nDeuxieme test\n')

p = np.array([0.5, 4.])
print('le point initial est ', p)
dists = dataCreation(p)
print('les distance et la valeur correspondante de la fonction price sont')
print(dists, priceFunction(p, dists), '\n')


# # nelder-mead
# res = minimize(priceFunction, p, args=(dists),
#                method='nelder-mead',
#                options={'xtol': 1e-7, 'disp': True})
# print("\nla methode nelder-mead produit le point", res.x)
# print('la valeur pour ce point est', priceFunction(res.x, dists))
# # print(' ')
# # print("l'optimisation naive produit le point",
# #       naiveOptimization(3., 6., 1., 5., dists, 200), "\n\n")
# print(' ')
# #
# res = minimize(priceFunction, p, args=(dists),
#                method='BFGS',
#                options={'xtol': 1e-6, 'disp': True})
# print("\nla methode BFGS produit le point", res.x)



#######################################################################
### le dessin

fig = plt.figure(1, figsize=(14, 10))
fig.suptitle('Le probleme du recepteur (position vraie et position calculee)',
             fontsize=15)
axs = fig.add_subplot(111)
axs.set_aspect('equal')

plotProblem(p, -2, 11, -1, 9, 75, dists, fig, axs)
# plotCircle(sources[1], (1+ePercentages[1])*10., 150, 'magenta', fig, axs)

plt.show()

