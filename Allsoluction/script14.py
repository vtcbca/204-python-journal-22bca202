#Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.
import numpy as np
x = np.array([[0, 20, 40], [60, 80, 100]])
print("Original array: ")
print(x)
print("Values is bigger than 10 =", x[x>10])
