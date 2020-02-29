
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

from task1 import hybrid1, filterFFT
from task2 import hybrid2

def task3():
  n=input("Option(1,2): ")
  print("n: "+str(n))
  if n=="1":
    print("1")
    hyb=hybrid1(sys.argv[1],sys.argv[2],1.0,1.0)
    io.imshow(hyb)
    io.show()
  else:
    print("2")
    hyb=hybrid2(sys.argv[1],sys.argv[2],1.0,1.0)
    io.imshow(hyb)
    io.show()

  hyb=cv2.pyrDown(hyb)
  io.imshow(hyb)
  io.show()
 
  hyb=cv2.pyrDown(hyb)
  io.imshow(hyb)
  io.show()

  hyb=cv2.pyrDown(hyb)
  io.imshow(hyb)
  io.show()

task3()
