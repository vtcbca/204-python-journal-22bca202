#Write a NumPy program to create a new shape to an array without changing its data.

import numpy as np
A = np.array([1, 2, 3, 4, 5, 6])
B = np.reshape(x,(3,2))
print("Reshape 3x2:")
print(B)
C = np.reshape(x,(2,3))
print("Reshape 2x3:")
print(C)