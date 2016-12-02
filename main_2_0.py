'__author__' == 'qiuxuan.lin'       
# coding: utf-8                     
# Python 2.7.11


from datetime import datetime
from IPython import embed
import gc
import sys
sys.path.append('/Users/Shane/Documents/EC504_Network_Flow_Image_Segmentation/')
from image_process.GMM.proba import proba_gmm
from max_flow.mincut_fordfulkerson import mincut
from image_process.graph_utils import graph_penalty
from sklearn import decomposition
import cv2
import numpy as np
from math import*
from scipy.misc import imresize