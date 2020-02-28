# https://www.geeksforgeeks.org/gaussian-filter-generation-c/
# 
import numpy as np
import math
# 
# def makeGaussianFilter(rows, cols, sigma, highPass=True):
#   midrow = (rows+1)//2
#   midcol = (cols+1)//2
# 
# #  centerI = int(numRows/2) + 1 if numRows % 2 == 1 else int(numRows/2)
# #  centerJ = int(numCols/2) + 1 if numCols % 2 == 1 else int(numCols/2)
# 
#   def gaussian(i,j):
#     coefficient = math.exp(-1.0 * ((i - midrow)**2 + (j - midcol)**2) / (2 * sigma**2))
#     return 1 - coefficient if highPass else coefficient
# 
#   return np.array([[gaussian(i,j) for j in range(cols)] for i in range(rows)])
# 
# 
# 
# sigma = 255//2
# rows = int(input("Rows? "))
# cols = int(input("Cols? "))
# 
# arr = makeGaussianFilter(rows,cols,sigma)
# print("Guassian Filter")
# print(arr)

def gauss(k, r, c, sigma):
  rows,cols=r,c
  s=2.0*sigma*sigma
  cr=r//2
  cc=c//2
  sum=0.0
  print("cr, cc: "+str(cr)+" "+str(cc))
  for i in range(-cr,cr+1):
    for j in range(-cc,cc+1):
      r=math.sqrt(i*i+j*j)
      k[i+cr][j+cc]=math.exp(-r*r/s)/(math.pi*s) 
      sum+=k[i+cr][j+cc]

  print(type(r))
  print(type(c))

  for i in range(rows):
    for j in range(cols):
      k[i][j]/=sum
  return k

sigma = 255//2
rows = int(input("Rows? "))
cols = int(input("Cols? "))
arr = np.zeros((rows,cols))
arr = gauss(arr,rows,cols,1.0)
print("Guassian Filter")
print(arr)



# // function to create gaussian filter 
# void filtercreation(double gkernel[][5]) 
# { 
#     // intialising standard deviation to 1.0 
#     double sigma = 1.0; 
#     double r, s = 2.0 * sigma * sigma; 
#   
#     // sum is for normalization 
#     double sum = 0.0; 
#   
#     // generating 5x5 kernel 
#     for (int x = -2; x <= 2; x++) { 
#         for (int y = -2; y <= 2; y++) { 
#             r = sqrt(x * x + y * y); 
#             gkernel[x + 2][y + 2] = (exp(-(r * r) / s)) / (m_pi * s); 
#             sum += gkernel[x + 2][y + 2]; 
#         } 
#     } 
#   
#     // normalising the kernel 
#     for (int i = 0; i < 5; ++i) 
#         for (int j = 0; j < 5; ++j) 
#             gkernel[i][j] /= sum; 
# } 
#   
# // driver program to test above function 
# int main() 
# { 
#     double gkernel[5][5]; 
#     filtercreation(gkernel); 
#   
#     for (int i = 0; i < 5; ++i) { 
#         for (int j = 0; j < 5; ++j) 
#             cout << gkernel[i][j] << "\t"; 
#         cout << endl; 
#     } 
# }
