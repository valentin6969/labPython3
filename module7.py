import numpy as np
import scipy.interpolate as interpolate

H=[7,10,11,15,19]
T=[7,12,13,15,13]
f=interpolate.interp1d(H,T, kind='cubic')
print(f([9.75,12,17]))
