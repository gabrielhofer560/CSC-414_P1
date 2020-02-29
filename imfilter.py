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

def imfilter2(A,kernel):
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

def imfilter(A,kernel): 
  if kernel.shape[0]%2==0 or kernel.shape[1]%2==0 : 
    print("Error: Invalid kernel dimensions. Quitting...")
    return A
  if(len(A.shape)==2): 
    imfilter2(A,kernel)
  if(len(A.shape)>2): 
    for i in range(A.shape[2]):
      A[:,:,i] = imfilter2(A[:,:,i],kernel)
  return A

def main():
  for FILE in sys.argv[1:]:
    A = cv2.imread(filename)   # for not color?
  # A = io.imread(filename)  # for color?
    B = imfilter(A,outline)
    io.imsave("out.png",B)
    plt.imshow(B)
    plt.show()

# main()



