#zad6
from scipy import integrate
def f(x,y):
    return x+y**2*x
x1=integrate.nquad(f,[[2,3],[0,2]])
print(x1)
