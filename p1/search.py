
# Sample code for generation of first example 
import numpy as np 
# from matplotlib import pyplot as plt 
# pyplot imported for plotting graphs 
  
x = np.linspace(0, 0, 9) 
  
# numpy.linspace creates an array of 
# 9 linearly placed elements between 
# -4 and 4, both inclusive  
y = np.linspace(-5, 5, 11) 
  
# The meshgrid function returns 
# two 2-dimensional arrays  
x_1, y_1 = np.meshgrid(x, y) 
  
print("x_1 = ") 
print(x_1) 
print("y_1 = ") 
print(y_1) 