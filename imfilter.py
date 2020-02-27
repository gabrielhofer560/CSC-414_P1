import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float32
import sys
import matplotlib.image as mpimg

from skimage import color

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
  [-1,9,-1],
  [0,-1,0]
  ])

#--------------------------------------------------------------------
def make_blur_kernel(dim):
  blur = np.full((dim,dim),1/(dim*dim))
  return blur
kernel3 = make_blur_kernel(7)

#--------------------------------------------------------------------
def rgb2gray(A):
  print("dimensions: ")
  print(A.shape)
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

#--------------------------------------------------------------------
def im_filter_color(A,kernel):

  (mi,ni,ki) = A.shape
  (mk,nk) = kernel.shape

  Z = np.zeros((mi+mk,ni+nk,ki))
  tmp = np.zeros((mi+mk,ni+nk,ki))

  for i in range(mi):
    for j in range(ni):
      for k in range(ki):
        Z[i+mk//2][j+nk//2][k]=A[i][j][k]

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

  for i in range(mi):
    for j in range(ni):
      for p in range(ki):
        A[i][j][p]=tmp[i+mk//2][j+nk//2][p]

  return A

#--------------------------------------------------------------------
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

  return A

#--------------------------------------------------------------------
def my_imfilter(filename,kernel): # ,mode,boundary):
  A = rgb2gray(io.imread(FILE))
  plt.imshow(A)
  plt.show()

  print("shape after rgb2gray")
  print(A.shape)

  if(len(A.shape)==2): 
    im_filter_gray(A,kernel)
  if(len(A.shape)>2): 
    im_filter_color(A,kernel)


#--------------------------------------------------------------------
def main():
  for FILE in sys.argv[1:]:
    B = my_imfilter(FILE,sharpen)
    plt.imshow(B)
    plt.show()

main()






 
