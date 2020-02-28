### Task 2
### Getting our "Feet Wet"
### How to hybrid images with gaussian filtering:
### https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/html/agartia3/index.html


import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import misc
from scipy import ndimage
import math
from skimage import io
import sys

from gaussian import gauss
from imfilter import imfilter
import cv2


def hybrid(A,B,sigH,sigL):

  h=imfilter(A, gauss(3,3,sigH))
  l=imfilter(B, gauss(3,3,sigL))

  A = io.imread(sys.argv[1])   
  h= A-h

  #B = io.imread(sys.argv[2])
  #l= B-l

#  C = h < 0
#  h[C] = 0
#  D = h > 255
#  h[D] = 255

  for i in range(h.shape[0]):
    for j in range(h.shape[1]):
      for k in range(h.shape[2]):
        h[i][j][k] = h[i][j][k]/2
        l[i][j][k] = l[i][j][k]/2

  result = l + h

  io.imshow(result)
  io.show()

  io.imsave("high.png",h)
  io.imsave("low.png",l)
  return h+l

def main():
  print("opening files: "+str(sys.argv[1])+", "+str(sys.argv[2]))
  sigH=int(input("sigma high: "))
  sigL=int(input("sigma low: "))

  A = io.imread(sys.argv[1])   # for not color?
  B = io.imread(sys.argv[2])   # for not color?

  result = hybrid(A,B,sigH,sigL)
  io.imsave("out.png",result)

main()


