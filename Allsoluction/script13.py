#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

#Output will print dimension and size of each element and array in memory.

import numpy as np
A=  np.arange(5, 10).reshape(6,6)
print(A)