from matplotlib.pyplot import imread, imsave
import numpy as np
img = imread('obraz1.png')
img2= np.flip(img,axis=0)
img[img2<0.75]=img2[img2<0.75]
img2=np.flip(img,axis=1)
img[img2<0.75]=img2[img2<0.75]
imsave('obraz_test1.png', img)
