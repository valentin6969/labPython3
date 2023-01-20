import matplotlib.pyplot as plt
import numpy as np 
import math as m
from matplotlib import cm

D = np.loadtxt('hist.txt', delimiter= ',')
plt.hist(D[:,1],bins=6, rwidth=0.7, color='green', 
         label=np.unique(D[:,1]))
plt.show()