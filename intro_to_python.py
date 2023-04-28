# Goudi Dwaish
# COT4500-23Spring 0001
# JAN 25, 2023
# Intro to GetHub and Python
# Professor Juna Parra

import numpy as np

# #1
matrix1 = np.eye(3)
print(matrix1)

# #2
matrix2 = matrix1 + 3 * (1 - np.eye(3))
print(matrix2)

# #3
matrix3 = np.delete(matrix2, -1, axis=1)
print(matrix3)
