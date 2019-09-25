import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# quelques fonctions
def anF(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))

def easom(a, b):
    E = -np.cos(a)*np.cos(b)*np.exp(-((a-np.pi/2)**2+(b-3./4)**2))
    return E

def P(x, y):
    E = (1.5-x+x*y)**2 + (2.25-x+x*y**2)**2 + (2.625-x+x*y**3)**2
    return E

def Q0(x, y):
    E = x**4 +2*y**4 -2*x**2*y +x*y -y
    return E

def Q(x, y):
    E = (x**2 +y -4)**2 + (x +y**2)**2
    return E

def R(x, y):
    E = (x**2 +y -4)**2 +x**2 +y**2
    return E


####################################################################
# les donnees d'entree

F = Q0
xmin = -3.5
xmax = 3.3
ymin = -3.5
ymax = 3.5
Nx = 100  # nombre de points utilises sur l'axe des x
Ny = 100  # nombre de points utilises sur l'axe des y
nbOfLevels = 250

#####################################################################

x = np.linspace(xmin, xmax, Nx)
y = np.linspace(ymin, ymax, Ny)

X, Y = np.meshgrid(x, y)
Z_fg = F(X, Y)  # foreground


# create the figure using the add_subplot command
fig = plt.figure(figsize=(15, 10), frameon=False)
fig.suptitle('Utilisant add_subplot', fontsize=15)
extent = xmin, xmax, ymin, ymax

'''
On utilise la commande
  fig.add_subplot(nb of rows, nb of columns, index) 
Les arguments sont, ou bien un entier avec trois posiitons, ou bien 
trois entiers separes ; ils decrivent les positions des sous-figures.
Si les entiers sont L, C et P (dan dans le plan,s cet ordre), alors le 
sous-figure aura la position P sur une grille ayant L linges et C 
colonnes.
'''

# Dans notre cas, la figure est representee comme une grille de
# taille 2x2.  On commence par la position (1,1) de la grille.
ax_1 = fig.add_subplot(2, 2, 1, aspect='equal') 
cs_1 = ax_1.contour(X, Y, Z_fg, nbOfLevels, cmap=mpl.cm.brg)
fig.colorbar(cs_1, ax=ax_1)
ax_1.title.set_text('courbes de niveau -- brg colormap')



# la position  (1,2) 
ax_2 = fig.add_subplot(2,2,2, aspect='equal') # , facecolor='yellow')
cs_2 = ax_2.contourf(X, Y, Z_fg, nbOfLevels, cmap=mpl.cm.nipy_spectral,
                     alpha=.99)
fig.colorbar(cs_2, ax=ax_2)
ax_2.title.set_text('courbes de niveau "filled" -- nipy_spectral colormap')



# la position (2,1), i.e. le troisieme element
ax_3 = fig.add_subplot(2,2,3, projection='3d')
ax_3.set_zlim(-1.01, 200.)
cs_3 = ax_3.plot_surface(X, Y, Z_fg, cmap=mpl.cm.plasma, #Blues_r,
                         linewidth=0, antialiased=False)
ax_3.title.set_text('representation 3d -- plasma colormap')



# la position (2,2), i.e. le dernier element
ax_4 = fig.add_subplot(2,2,4)

Z_bg = np.add.outer(range(8), range(8)) % 2  # chessboard
im4_backg = ax_4.imshow(Z_bg, cmap=plt.cm.gray,
                        interpolation='nearest', extent=extent)
im4_foreg = ax_4.imshow(Z_fg, cmap=plt.cm.gnuplot, alpha=.9, extent=extent)
ax_4.invert_yaxis()
ax_4.title.set_text('avec imshow -- gnuplot colormap')
# imshow est utilise d'habitude pour introduire une image dans la figure
# la variable alpha controle la transparence

plt.show()



