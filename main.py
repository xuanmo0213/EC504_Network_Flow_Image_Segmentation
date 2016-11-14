
# coding: utf-8
# Python 2.7.11

'__author__' == 'qiuxuan.lin'


from datetime import datetime
from IPython import embed
import gc
import sys
sys.path.append('/Users/Shane/Documents/EC504_Network_Flow_Image_Segmentation/')
from image_process.GMM.proba import proba_gmm
from max_flow.mincut_fordfulkerson import mincut
from sklearn import decomposition
import cv2
import numpy as np
from apgl.graph import SparseGraph


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

    centroid, pixel_proba, model = proba_gmm(Z,16, 'diag')
    gc.collect()
    pca = decomposition.PCA(2, whiten= True)
    reduced_proba = pca.fit_transform(pixel_proba)

    reduced_proba = sigmoid_array(reduced_proba)
    label = reduced_proba.argmax(axis = 1)
    center = centroid[1:3]
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    print "End processing: ", datetime.now()

    cv2.imshow('img', img)
    cv2.imshow('gmmed with PCA', res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gc.collect()
    # embed()


    a = np.ceil(np.array(reduced_proba[:,0]*10))
    b = np.ceil(np.array(reduced_proba[:,1]*10))

    n = len(a) #total number of pixels - internal "nodes"
    graph = [[0 for col in range(n+2)] for row in range(n+2)]

    for i in range(1,n+1):
        graph[0][i], graph[i][n+1] = int(a[i-1]), int(b[i-1])
        for j in range(1,n+1):
            graph[i][j] = 1



    src = 0  # source node
    sink = n + 1  # sink node
    V = n+2
    print "Matrix dimension V = ", V, datetime.now()
    mincut(graph, src, sink, V)

    print "Reconstructing Image ...", datetime.now()