# zadanie 3
import numpy as np
Data = np.loadtxt('contact-lenses.txt', delimiter = ',',
                 dtype = [('age', 'bytes', 14),('spectacle-prescrip', 'bytes', 12),  ('astigmatism', 'bytes', 5), ('tear-prod-rate', 'bytes', 7), ('contact-lenses', 'bytes', 4)])


Data['age'] = np.char.upper(Data['age'])
print(Data)
Data['spectacle-prescrip'] = np.char.upper(Data['spectacle-prescrip'])
Data['astigmatism'] = np.char.upper(Data['astigmatism'])
Data['tear-prod-rate'] = np.char.upper(Data['tear-prod-rate'])
Data['contact-lenses'] = np.char.upper(Data['contact-lenses'])

Data['astigmatism'] = np.char.replace(Data['astigmatism'], b'NO', b'FALSE')
Data['astigmatism'] = np.char.replace(Data['astigmatism'], b'YES', b'TRUE')
print(Data)
np.savetxt('contact-lenses-res.txt', Data, delimiter = ',', fmt='%s')