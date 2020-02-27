# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/
# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/html/ychen918/index.html
# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj1/html/zlu83/
# https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/

# http://cs.brown.edu/courses/csci1430/2013/results/proj1/
# http://cs.brown.edu/courses/csci1430/2013/results/proj1/xl76/
import time
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float32
import sys

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

def make_blur_kernel(dim):
  blur = np.full((dim,dim),1/(dim*dim))
  return blur
kernel3 = make_blur_kernel(7)

def my_imfilter(image,kernel,filename): # ,mode,boundary):

  # https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html
  A = io.imread(filename)

  # print("kernel3: ")
  # print(kernel3)

#  A = np.zeros((9,9))
#  for i in range(9):
#    for j in range(9):
#      A[i][j]= 9*9/2
  
  # print("this is A: ")
  # print(A)

  if(len(A.shape)==2):
    (mi,ni) = A.shape
    (mk,nk) = kernel.shape
  if(len(A.shape)==3):
    (mi,ni,ki) = A.shape
    (mk,nk,kk) = kernel.shape

  plt.imshow(A)
  plt.show()

  Z = np.zeros((mi+mk,ni+nk))
  for i in range(mi):
    for j in range(ni):
      Z[i+mk//2][j+nk//2]=A[i][j]

  # print(Z)
  plt.imshow(Z)
  plt.show()

  for i in range(mi):
    for j in range(ni):
      acc=0
      for k in range(mk):
        for l in range(nk):
          acc+=Z[i+k][j+l]*kernel[k][l]
      # print("acc: "+str(acc))
      Z[i+mk//2][j+nk//2]=acc

  # Z = np.zeros((mi+mk,ni+nk))
  for i in range(mi):
    for j in range(ni):
      A[i][j]=Z[i+mk//2][j+nk//2]

  # print(Z)
  plt.imshow(A)
  plt.show()

for FILE in sys.argv[1:]:
  my_imfilter(FILE,kernel3,FILE)





# import time
# import skimage
# from skimage import io
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage import img_as_float32
# import sys
# 
# # start the timer
# start = time.time()
# 
# def process(file):
#   A = io.imread(file)
#   (m1,n1) = A.shape
#   
#   plt.imshow(A)
#   plt.show()
#   
#   # logical indexing to set values less than 10 to 0
#   B = A < 80
#   A[B] = 0
#   
#   # display the image after changes
#   plt.imshow(A)
#   plt.show()
#   
#   # stop the timer and display elapse time to modify image
#   end = time.time()
#   print("total time: "+str(end - start))
# 
# # read the image
# for file in sys.argv[1:]:
#   process(file)
# 
# 
