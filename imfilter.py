# https://en.wikipedia.org/wiki/Convolutional_neural_network
import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float32
import sys
import matplotlib.image as mpimg
from skimage import color
import cv2

### Some Kernels:
indentity = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0]])

blur = np.array([
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]
    ])

sharpen = np.array([
  [0,-1,0],
  [-1,5,-1],
  [0,-1,0]
  ])

emboss = np.array([
  [-2,-1,0],
  [-1,1,1],
  [0,1,2]
  ])

left_sobel = np.array([
  [1,0,-1],
  [2,0,-2],
  [1,0,-1]
  ])

outline = np.array([
  [-1,-1,-1],
  [-1,8,-1],
  [-1,-1,-1]
  ])

def make_blur_kernel(dim):
  blur = np.full((dim,dim),1/(dim*dim))
  return blur
kernel3 = make_blur_kernel(7)

def rgb2gray(A):
  (a, b, c) = A.shape
  ret = np.zeros((a, b))
  for j in range(a):
    for k in range(b):
      acc=0
      for i in range(c):
        acc+=A[j][k][i]
      acc/=c
      ret[j][k]=acc
  return ret

def imfilter2(A,kernel):
  #print(kernel)
  (mi,ni) = A.shape
  (mk,nk) = kernel.shape
  Z = np.zeros((mi+mk,ni+nk))
  tmp = np.zeros((mi,ni))
  for i in range(mi):
    for j in range(ni):
      Z[i+mk//2][j+nk//2]=A[i][j]
  for i in range(mi):
    for j in range(ni):
      acc=0
      for k in range(mk):
        for l in range(nk):
          acc+=(Z[i+k][j+l]*kernel[k][l])
      if(acc<0): acc=0
      if(acc>255): acc=255
      tmp[i][j]=acc

  for i in range(mi):
    for j in range(ni):
      A[i][j]=tmp[i][j]
  return A

def imfilter(filename,kernel): # ,mode,boundary):
  A = cv2.imread(filename)
  # A = io.imread(filename) 
  plt.imshow(A)
  plt.show()

  if(len(A.shape)==2): 
    imfilter2(A,kernel)
  if(len(A.shape)>2): 
    for i in range(A.shape[2]):
      A[:,:,i] = imfilter2(A[:,:,i],kernel)
  return A

def main():
  for FILE in sys.argv[1:]:
    B = imfilter(FILE,outline)
    io.imsave("out.png",B)
    plt.imshow(B)
    plt.show()

main()



