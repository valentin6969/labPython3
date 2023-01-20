import numpy as np
def zad2(n):
    A=np.zeros((n,n), dtype=int)
    for w in range (0, n):
        if w%2==0:
            A[w,:]=np.array(range(w*n+1, (w+1)*n+1))
        else:
            A[w,:]=np.array(range((w+1)*n, w*n,-1))
    return A
print(zad2(4))

