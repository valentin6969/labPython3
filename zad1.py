import numpy as np
# zadanie 1

Data = np.loadtxt('irisP.txt', delimiter = ',', 
                  usecols = (3,4), dtype = [('szerokosc_platka', 'float'), ('class', 'bytes', 17)])
setosa = Data['class'] == b'Iris-setosa'
versicolor = Data['class'] == b'Iris-versicolor'
virginica = Data['class'] == b'Iris-virginica'
print('Iris-setosa: ', Data['szerokosc_platka'][setosa].mean())
print('Iris-versicolor: ', Data['szerokosc_platka'][versicolor].mean())
print('Iris-virginica: ', Data['szerokosc_platka'][virginica].mean())