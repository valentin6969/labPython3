import matplotlib.pyplot as plt
import numpy as np 
import math as m
from matplotlib import cm

X=np.random.normal(0,1,1024)
Y=np.random.normal(0,1,1024)
Z=(np.round(X)+np.round(Y))%2
plt.figure()
plt.scatter(X,Y,c=Z, s=50, alpha = 0.5)

plt.show()