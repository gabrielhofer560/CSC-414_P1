# https://www.geeksforgeeks.org/gaussian-filter-generation-c/
import numpy as np
import math

def gauss(r, c, sigma, highPass):
  k=np.zeros((r,c))
  rows,cols=r,c
  s=2.0*sigma*sigma
  cr=r//2
  cc=c//2
  sum=0.0
  print("cr, cc: "+str(cr)+" "+str(cc))
  for i in range(-cr,cr+1):
    for j in range(-cc,cc+1):
      r=math.sqrt(i*i+j*j)
      if highPass: k[i+cr][j+cc]=1-math.exp(-r*r/s)/(math.pi*s) 
      else : k[i+cr][j+cc]=math.exp(-r*r/s)/(math.pi*s) 
      sum+=k[i+cr][j+cc]
  for i in range(rows):
    for j in range(cols):
      k[i][j]/=sum
  return k


def main():
  sigma = 255//2 
  rows = int(input("Rows? "))
  cols = int(input("Cols? "))
  h = int(input("high pass? "))
  arr = np.zeros((rows,cols))
  arr = gauss(rows,cols,128,h)
  print("Guassian Filter")
  print(arr)

 



# main()












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
