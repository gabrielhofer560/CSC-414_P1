// https://www.geeksforgeeks.org/gaussian-filter-generation-c/
#include <cmath> 
#include <iomanip> 
#include <iostream> 
using namespace std; 
  

// function to create gaussian filter 
void filtercreation(double gkernel[][5]) 
{ 
    // intialising standard deviation to 1.0 
    double sigma = 1.0; 
    double r, s = 2.0 * sigma * sigma; 
  
    // sum is for normalization 
    double sum = 0.0; 
     
    // generating 5x5 kernel 
    for (int x = -2; x <= 2; x++) { 
        for (int y = -2; y <= 2; y++) { 
            r = sqrt(x * x + y * y); 
            gkernel[x + 2][y + 2] = (exp(-(r * r) / s)) / (M_PI * s); 
            sum += gkernel[x + 2][y + 2]; 
        } 
    } 
  
    // normalising the kernel 
    for (int i = 0; i < 5; ++i) 
        for (int j = 0; j < 5; ++j) 
            gkernel[i][j] /= sum; 
} 
  
// driver program to test above function 
int main() 
{ 
    double gkernel[5][5]; 
    filtercreation(gkernel); 
  
    for (int i = 0; i < 5; ++i) { 
        for (int j = 0; j < 5; ++j) 
            cout << gkernel[i][j] << "\t"; 
        cout << endl; 
    } 
} 
