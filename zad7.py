import matplotlib.pyplot as plt
import numpy as np 
import math as m
from matplotlib import cm

x = np.linspace( -2 ,2 ,256)
y = np.linspace( -2 ,2 ,256) 
X , Y = np.meshgrid(x , y )
Z = -y **3 + X **2 + Y **2 + 2* X - 1
plt.contourf(X,Y,Z, levels=10, alpha=0.7,
    cmap=cm.hot, lw=0.5)


plt.show()