
from matplotlib.pyplot import imread, imsave
img = imread('logo.png')
img = 1-img
imsave('logo2.png', img)
