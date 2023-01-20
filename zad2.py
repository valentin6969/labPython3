import numpy as np
from numpy import linalg
def Cramer(A, B):
    n = len(A[0])
    X=np.zeros((1, len(A[0])))
    W = np.linalg.det(A)
    for i in range(n):
        Wi = W.copy()
        Wi[:, i]=B.flatten()
        Wi=np.linalg.det(Wi)
        X[:,i]=Wi/W
    return X
A=np.arange(-10,15, 1)
A=np.resize(A,(5,5))
B=np.array([[1],[2],[3],[4],[5]])
print(A)
print(Cramer(A,B))
