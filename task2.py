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


def high(img,sig):
  print("SIG: "+str(sig))
  return imfilter(img,gauss(3,3,sig,1))

def low(img,sig):
  return imfilter(img,gauss(3,3,sig,0))

def hybrid(im1,im2,sigH,sigL):
  h=high(im1,sigH)
  l=low(im2,sigL)
  return high(im1,sigH) + high(im2,sigL)

def main():
  print("opening files: "+str(sys.argv[1])+", "+str(sys.argv[2]))
  sigH=int(input("sigma high: "))
  sigL=int(input("sigma low: "))
  result = hybrid(sys.argv[1],sys.argv[2],sigH,sigL)
  io.imsave("task2_out.png")

main()


