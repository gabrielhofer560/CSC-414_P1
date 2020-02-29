### Task 2
### Getting our "Feet Wet"
### How to hybrid images with gaussian filtering:
### https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/html/agartia3/index.html

import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import misc
from scipy import ndimage
import math
from skimage import io
import sys

from gaussian import gauss
from imfilter import imfilter
import cv2

def hybrid2(F1,F2,sigH,sigL):
  A = io.imread(F1)   # for not color?
  B = io.imread(F2)   # for not color?
  l=imfilter(A, gauss(5,5,sigH))
  h=imfilter(B, gauss(5,5,sigL))
  A = io.imread(F1)
  l = A-l
  for i in range(h.shape[0]):
    for j in range(h.shape[1]):
      for k in range(h.shape[2]):
        h[i][j][k] = h[i][j][k]/2
        l[i][j][k] = l[i][j][k]/2
  return (l + h)

def main():
  hyb = hybrid2(sys.argv[1],sys.argv[2],1.0,1.0)
  io.imshow(hyb)
  io.show()
  io.imsave("out.png",hyb)
#main()


