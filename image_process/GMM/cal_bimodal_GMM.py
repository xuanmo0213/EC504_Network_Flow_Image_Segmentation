# This example is from http://stackoverflow.com/questions/37300698/gaussian-mixture-model-fit-in-python-with-sklearn-is-too-slow-any-alternative
# Not Yet Tested

import cv2
import numpy as np
import math
from sklearn.mixture import GMM

im = cv2.imread('Boat.jpg');

h, w, _ = im.shape;       # Height and width of the image

# Extract Blue, Green and Red
imB = im[:,:,0]; imG = im[:,:,1]; imR = im[:,:,2];

# Reshape Blue, Green and Red channels into single-row vectors
imB_V = np.reshape(imB, [1, h * w]);
imG_V = np.reshape(imG, [1, h * w]);
imR_V = np.reshape(imR, [1, h * w]);

# Combine the 3 single-row vectors into a 3-row matrix
im_V =  np.vstack((imR_V, imG_V, imB_V));

# Calculate the bimodal GMM
nmodes = 2;
GMModel = GMM(n_components = nmodes, covariance_type = 'full', verbose = 0, tol = 1e-3)
GMModel = GMModel.fit(np.transpose(im_V))