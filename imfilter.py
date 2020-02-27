# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/
# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/html/ychen918/index.html
# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/html/zlu83/
# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/

# http://cs.brown.edu/courses/csci1430/2013/results/proj1/
# http://cs.brown.edu/courses/csci1430/2013/results/proj1/xl76/

# mode 
# boundary 

import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float32
import sys
import matplotlib.image as mpimg

from skimage import color
# img = color.rgb2gray(io.imread('image.png'))
# https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

# https://docs.scipy.org/doc/numpy/user/basics.creation.html
kernel0 = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0]])

kernel2 = np.zeros((5,5))
kernel2[2][2]=1

kernel1 = np.array([
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]
    ])

sharpen = np.array([
  [0,-1,0],
  [-1,9,-1],
  [0,-1,0]
  ])

def make_blur_kernel(dim):
  blur = np.full((dim,dim),1/(dim*dim))
  return blur
kernel3 = make_blur_kernel(7)

# def rgb2gray(A):
#   print("dimensions: ")
#   print(A.shape)
#   (a, b, c) = A.shape
#   ret = np.zeros((a, b))
#   for j in range(a):
#     for k in range(b):
#       acc=0
#       for i in range(c):
#         acc+=A[j][k][i]
#       acc/=c
#       ret[j][k]=acc
#   return ret

def im_filter_color(A,kernel):

  (mi,ni,ki) = A.shape
  (mk,nk) = kernel.shape

  Z = np.zeros((mi+mk,ni+nk,ki))
  tmp = np.zeros((mi+mk,ni+nk,ki))

  print("here")

  for i in range(mi):
    for j in range(ni):
      for k in range(ki):
        Z[i+mk//2][j+nk//2][k]=A[i][j][k]

  print("here2")


  for p in range(ki):
    print(str(p)+" th channel")
    for i in range(mi):
      print("\t"+str(i)+"/"+str(mi))
      for j in range(ni):
        acc=0
        for k in range(mk):
          for l in range(nk):
            acc+=Z[i+k][j+l][p]*kernel[k][l]
        tmp[i+mk//2][j+nk//2][p]=acc

  for p in range(ki):
    for i in range(mi):
      for j in range(ni):
        A[i][j][p]=tmp[i+mk//2][j+nk//2][p]

#  print(A[0])
#  print()
#  print(A[1])
#  print()
#  print(A[2])
#  print()
  plt.imshow(A)
  plt.show()

def im_filter_gray(A,kernel):

  (mi,ni) = A.shape
  (mk,nk) = kernel.shape

  Z = np.zeros((mi+mk,ni+nk))
  tmp = np.zeros((mi+mk,ni+nk))
  for i in range(mi):
    for j in range(ni):
      Z[i+mk//2][j+nk//2]=A[i][j]

  plt.imshow(Z)
  plt.show()

  for i in range(mi):
    for j in range(ni):
      acc=0
      for k in range(mk):
        for l in range(nk):
          acc+=Z[i+k][j+l]*kernel[k][l]
      tmp[i+mk//2][j+nk//2]=acc

  for i in range(mi):
    for j in range(ni):
      A[i][j]=tmp[i+mk//2][j+nk//2]

  plt.imshow(A)
  plt.show()

def my_imfilter(filename,kernel): # ,mode,boundary):
  A = io.imread(FILE)
  plt.imshow(A)
  plt.show()

  if(len(A.shape)==2): 
    im_filter_gray(A,kernel)
  if(len(A.shape)>2): 
    im_filter_color(A,kernel)


# B = np.zeros((9,9,3))
# for i in range(9): 
#   for j in range(9):
#     for k in range(3):
#       B[i][j][k]=40

for FILE in sys.argv[1:]:
  my_imfilter(FILE,kernel1)



 
