import numpy as np

Data = np.genfromtxt('irisP.txt',
                    delimiter = ',',
                   usecols = (4), dtype = [('class', 'bytes', 17)])
Data['class']=np.char.replace(Data['class'], b'Iris-', b'')
np.savetxt('iris-res.txt', Data, fmt='%s')
