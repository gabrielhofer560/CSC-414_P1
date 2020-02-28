# https://www.geeksforgeeks.org/gaussian-filter-generation-c/
import numpy as np
import math

def gauss(r, c, sigma):
  k=np.zeros((r,c))
  rows,cols=r,c
  s=2.0*sigma*sigma
  cr=r//2
  cc=c//2
  sum=0.0
  for i in range(-cr,cr+1):
    for j in range(-cc,cc+1):
      r=math.sqrt(i*i+j*j)
      k[i+cr][j+cc]=math.exp(-r*r/s)/(math.pi*s) 
      sum+=k[i+cr][j+cc]
  for i in range(rows):
    for j in range(cols):
      k[i][j]/=sum
  return k


def main():
  sigma = 255//2 
  sigma = int(input("sigma? "))
  rows = int(input("Rows? "))
  cols = int(input("Cols? "))
  arr = np.zeros((rows,cols))
  arr = gauss(rows,cols,sigma)
  print("Guassian Filter")
  print(arr)

#main()


