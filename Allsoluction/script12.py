#scrip12....Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array. Print original list and array with its dimension , size and byte occupied in memory
import numpy as np
l = [50, 100, 200, 332,400,500]
print("A Original List:",l)
A = np.array(l)
print("One-dimensional NumPy array: ",A)
