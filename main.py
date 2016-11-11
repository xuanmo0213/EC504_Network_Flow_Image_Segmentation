
# coding: utf-8
# __author__ = qiuxuan.lin


from datetime import datetime
from IPython import embed
import gc
import sys
sys.path.append('/Users/Shane/Documents/EC504_Network_Flow_Image_Segmentation/')
from image_process.GMM.proba import proba_gmm
# from max_flow.image_seg import
from sklearn import decomposition
import cv2
import numpy as np


def sigmoid_array(x):
  return 1 / (1 + np.exp(-x))

if __name__ == '__main__':
    if len(sys.argv[1]) < 3:
        print "Please specify the name of your image!"
        exit()

    print "Start processing image: ", datetime.now()
    image_in = sys.argv[1]
    # image_out = sys.argv[2]

    img = cv2.imread(image_in)
    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    centroid, pixel_proba, model = proba_gmm(Z,2, 'diag')
    print "End processing: ", datetime.now()

    # pca = decomposition.PCA(2, whiten= True)
    # reduced_proba = pca.fit_transform(pixel_proba)
    #
    #
    # label = sigmoid_array(reduced_proba).argmax(axis = 1)
    # center = centroid[0:2]
    # res = center[label.flatten()]
    # res2 = res.reshape((img.shape))
    #
    # cv2.imshow('img', img)
    # cv2.imshow('gmmed', res2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # embed()




