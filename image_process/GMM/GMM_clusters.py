
# coding: utf-8
# __author__ = qiuxuan.lin


import cv2
import numpy as np
from sklearn import mixture
from IPython import embed
# import matplotlib.pyplot as plt


img = cv2.imread('simple.jpg')

g = mixture.GMM(n_components=8) # tried 'full' or 'spherical' no improvememts
Z = img.reshape((-1,3))
Z = np.float32(Z)

g.fit(Z)

label = g.predict(Z)
center = g.means_ # centroid RGB values
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))



cv2.imshow('img', img)
cv2.imshow('gmmed', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

