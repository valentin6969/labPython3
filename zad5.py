import numpy as np

L={1:[2,4,6],2:[3],3:[], 4:[], 5:[4,5], 6:[3]}
n= len(L)
S=np.zeros((n,n))
m=np.sum([len(i) for i in L.values()])
J=np.zeros((n,m))
k=0
for key in L:
    for value in L[key]:
        S[key-1,value-1]=1
        J[key-1,k]=1
        J[value-1,k]=1
        if key==value:
            J[key-1, k]=2
        k+=1
print(S)
print(J)

