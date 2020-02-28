### Task 1
### Getting our "Feet Wet"

import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import misc
from scipy import ndimage
import math
from skimage import io
import sys




def high():

def low():

def hybrid(im1,im2,sigH,sigL):
  return high(im1,sigH) + low(im2,sigL)

def main():
  print("opening files: "+str(sys.argv[1])+", "+str(sys.argv[2]))
  im1 = io.imread(sys.argv[1])
  im2 = io.imread(sys.argv[2])
  sigH=int(input("sigma high: "))
  sigL=int(input("sigma low: "))
  result = hybrid(im1,im2,sigH,sigL)



main()


