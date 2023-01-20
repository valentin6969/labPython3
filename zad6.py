import numpy as np
def zad6(n,m):
    A=np.random.randint(2,22,(m,n))
    A[np.mod(A,2)==0]=-100
    A[np.mod(A,2)==1]=100
    return A

