import numpy as np

# zadanie 5
def fun(x,y):
	return x**2+3*y**2

def pso(n, it, XYmin, XYmax):
	P = np.concatenate((np.random.rand(1,n)*(XYmax-XYmin) + XYmin, np.random.rand(1,n)*(XYmax-XYmin) + XYmin), axis=0)
	Pbest = P
	tmp = np.argmin(fun(P[0,:], P[1,:]))
	Gbest = P[:,tmp]
	V = np.random.rand(2,n)*(np.abs(XYmax-XYmin)) + 2*XYmin
	for i in range(it):
		V = 0.8*V - 2*np.random.rand(len(V), len(V[0]))*(P - Pbest) - 2*np.random.rand(len(V), len(V[0]))*(P - np.reshape(Gbest.repeat(n), (2,n)))
		P = P + V
		id = fun(Pbest[0,:], Pbest[1,:]) > fun(P[0,:], P[1,:])
		Pbest[:,id] = P[:,id]
		tmp = np.argmin(fun(P[0,:], P[1,:]))
		if fun(Gbest[0], Gbest[1]) > fun(P[0,tmp], P[1,tmp]):
			Gbest = P[:,tmp]
	return (Gbest, fun(Gbest[0], Gbest[1]))

print(pso(100,20,-5,5))
