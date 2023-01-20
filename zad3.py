import numpy as np
from numpy import concatenate as c
A=np.ones((2,2))
B=np.zeros((2,1))
P1=c((B,A), axis = 1)
P1=c((P1,A), axis = 1)
P2=c((B.T,B.T), axis = 1)
P1P2=c((P1,P2), axis = 0)
P3=c((B.T,A), axis = 0)
P=c((P1P2,P3), axis = 1)

