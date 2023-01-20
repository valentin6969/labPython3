import numpy as np

# zadanie 2
Data = np.genfromtxt('irisP2.txt', skip_header = 1, missing_values = '?',
                    filling_values = -100, delimiter = ',',
                   usecols = (2,4), dtype = [('dlugosc_platka', 'float'), ('class', 'bytes', 17)])

setosa = (Data['class'] == b'Iris-setosa') & (Data['dlugosc_platka'] != -100)
srednia_dlugosc_setosa = Data['dlugosc_platka'][setosa].mean()
setosa2 = (Data['class'] == b'Iris-setosa') & (Data['dlugosc_platka'] == -100)
Data['dlugosc_platka'][setosa2] = np.round(srednia_dlugosc_setosa,1)

versicolor = (Data['class'] == b'Iris-versicolor') & (Data['dlugosc_platka'] != -100)
srednia_dlugosc_versicolor = Data['dlugosc_platka'][versicolor].mean()
versicolor2 = (Data['class'] == b'Iris-versicolor') & (Data['dlugosc_platka'] == -100)
Data['dlugosc_platka'][versicolor2] = np.round(srednia_dlugosc_versicolor,1)

virginica = (Data['class'] == b'Iris-virginica') & (Data['dlugosc_platka'] != -100)
srednia_dlugosc_virginica = Data['dlugosc_platka'][virginica].mean()
virginica2 = (Data['class'] == b'Iris-virginica') & (Data['dlugosc_platka'] == -100)
Data['dlugosc_platka'][virginica2] = np.round(srednia_dlugosc_virginica,1)

print(Data)