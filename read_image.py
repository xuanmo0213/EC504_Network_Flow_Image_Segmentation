import cv2
from PIL import Image
import numpy as np
import math
import random
im = cv2.imread("input4.jpg")
origin = im
gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
p = np.array(gray_image)
h, w = gray_image.shape
#print h, w
fgraph = [[0 for temp_row in range(h * w + 2)] for temp_col in range(h * w + 2)]
intensity = [0 for item in range(h * w)]
usermark = [0 for item in range(h * w)]
procImg = [[0 for temp_row in range(w)] for temp_col in range(h)]
arr = [[0 for temp_row in range(w)] for temp_col in range(h)]
#p = p.reshape(-1, p.shape[2])
print p

def setPoint(x,y,val):
	arr[x][y] = value

def bgcalc():
	im = origin
	im = cv2.canny(300,600,5,true);

def printimage():
	im = origin
	objcount = 0
	backcount = 0
	for i in range(w):
		for j in range(h):
			sum = 0
			ab = im[i][j]
			sum = sum + int(ab[0] + ab[1]*1000 + ab[2]*1000000)
			intensity[i*h + j] = sum
			usermark[i*h + j] = arr[i][j]
			if (arr[i][j] == 1):
				objcount = objcount + 1
			else:
				if (arr[i][j] == 2):
					backcount = backcount + 1
	n = h * w
	k = 10
	lam = 7
	r = [[0 for temp_row in range(2)] for temp_col in range(n)]
	b = [[0 for temp_row in range(n)] for temp_col in range(n)]
	max = 0
	x = 0
	cost = 1
	sigma = 2
	objcount = 1
	backcount = 1
	for i in range(n):
		r[i][0] = int(math.log(intensity[i]/objcount))
		r[i][1] = int(math.log(intensity[i]/backcount))
		for j in range(n):
			if ((j==(i-1)) or (j==(i+1)) or j==(i-h) or j==(i+h) ):
				b[i][j] = int(math.pow(math.e, -1*math.pow((intensity[i]-intensity[j])/(2*sigma*sigma), 2)))
			if ( j==(i+h-1) or j==(i+h+1) or j==(i-h-1) or j==(i-h+1)):
				b[i][j]= int((math.pow(math.e, -1*math.pow((intensity[i]-intensity[j])/(2*sigma*sigma), 2))*1.44))
				x = x + b[i][j]
		if x > max :
			max = x
	k = max + 1
	for i in range(0,n,10):
		usermark[i] = random.randint(1,2)
	for i in range(n):
		if usermark[i] == 2:
			fgraph[i][n + 1] = k
			fgraph[n + 1][i] = k
		else:
			if usermark[i] == 1:
				fgraph[i][n + 1] = 0
				fgraph[n + 1][i] = 0
			else:
				fgraph[i][n + 1] = lam * r[i][0]
				fgraph[n + 1][i] = lam * r[i][0]
	for i in range(n):
		for j in range(n):
			if((j==(i-1)) or (j==(i+1)) or j==(i-h) or j==(i+h) or j==(i+h-1) or j==(i+h+1) or j==(i-h-1) or j==(i-h+1)):
				fgraph[i][j]=b[i][j];
	print fgraph
		
printimage()
