from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 
import math as m
from matplotlib import cm

x = np.arange(-5,5,0.05)
y = np.arange(-5,5,0.05)

X,Y = np.meshgrid(x,y)
Z=np.sin(X)*np.cos(Y-1)

fig = plt.figure() 
ax = fig.gca(projection ='3d') 
ax.plot_surface(X,Y,Z, cmap=cm.codwarm)
plt.show()
