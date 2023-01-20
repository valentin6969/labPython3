#zad4
from scipy.optimize import minimize

def func(x):
    x1,x2=x
    return (x1+2*x**2-7)**2+(2*x1+x2-5)**2


result = minimize(func, [-10, 10], tol =1e-6, method = 'Nelder-Mead')
print(result.x)
