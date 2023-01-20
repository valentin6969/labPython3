import numpy as np
def zad1(n):
  A=np.zeros((n,n), dtype=int)
  for w in range(n):
    for k in range(n):
      A[w,k]=(w+1)**k
  return A
print(zad1(4))

