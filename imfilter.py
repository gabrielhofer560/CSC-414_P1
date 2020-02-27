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
  [-1,5,-1],
  [0,-1,0]
  ])

def make_blur_kernel(dim):
  blur = np.full((dim,dim),1/(dim*dim))
  return blur
kernel3 = make_blur_kernel(7)


# def im_filter_color(image,kernel):
#   plt.imshow(A)
#   plt.show()
# 
#   (mi,ni,ki) = A.shape
#   (mk,nk,kk) = kernel.shape
# 
#   Z = np.zeros((mi+mk,ni+nk,ki+kk))
#   for i in range(mi):
#     for j in range(ni):
#       for k in range(ki):
#         Z[i+mk//2][j+nk//2][k+kk//2]=A[i][j][k]
# 
#   plt.imshow(Z)
#   plt.show()
# 
#   for p in range(ki):
#     for i in range(mi):
#       for j in range(ni):
#         acc=0
#         for k in range(mk):
#           for l in range(nk):
#             acc+=Z[p][i+k][j+l]*kernel[p][k][l]
#         # print("acc: "+str(acc))
#         Z[p][i+mk//2][j+nk//2]=acc
# 
#   for i in range(mi):
#     for j in range(ni):
#       for k in range(ki):
#         A[i][j][k]=Z[i+mk//2][j+nk//2][k+kk//2]
# 
#   plt.imshow(A)
#   plt.show()
#   return 0
#   


def im_filter_gray(A,kernel):

  #  A = np.zeros((6,6))
#  for i in range(6):
#    for j in range(6):
#      A[i][j]=18

  (mi,ni) = A.shape
  (mk,nk) = kernel.shape

  Z = np.zeros((mi+mk,ni+nk))
  tmp = np.zeros((mi+mk,ni+nk))
  for i in range(mi):
    for j in range(ni):
      Z[i+mk//2][j+nk//2]=A[i][j]

  plt.imshow(Z)
  plt.show()

#  for i in range(mi):
#    for j in range(ni):
#      print(Z[i][j],end=" ")
#    print()

  for i in range(mi):
    for j in range(ni):
      acc=0
      for k in range(mk):
        for l in range(nk):
          acc+=Z[i+k][j+l]*kernel[k][l]
      tmp[i+mk//2][j+nk//2]=acc

  # Z = np.zeros((mi+mk,ni+nk))
  for i in range(mi):
    for j in range(ni):
      A[i][j]=tmp[i+mk//2][j+nk//2]

  print(A)
  plt.imshow(A)
  plt.show()

def my_imfilter(filename,kernel): # ,mode,boundary):
  from PIL import Image
  image = Image.open(FILE).convert("L")
  A = io.imread(FILE)
  plt.imshow(A)
  plt.show()

  if(len(A.shape)==2): im_filter_gray(A,kernel)
  if(len(A.shape)==3): im_filter_color(A,kernel)

  # https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html
for FILE in sys.argv[1:]:
  # my_imfilter(FILE,kernel3)
  my_imfilter(FILE,sharpen)



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
