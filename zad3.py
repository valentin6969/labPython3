


import matplotlib.pyplot as plt
import numpy as np 
import math as m
x = np.linspace(-m.pi, m.pi, 128)
x2= np.arange(-m.pi, m.pi, 0.5)
plt.figure()
plt.subplot(2,2,1)

plt.plot(x, np.cos(x), 'k', label='cos(x)')
plt.subplot(2,2,2)

plt.plot(x, np.sign(x), 'r', label='sign(x)')
plt.subplot(2,2,(3,4))

plt.plot(x2, np.sign(x2), 'go', label='punkty')

plt.title(label='idk')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend()
plt.show()