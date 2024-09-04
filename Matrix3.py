#Write a program to find the inverse, rank, determinant and eigen values of a given matrix.

import numpy as np
a1 = np.array([[1, 2, 3], [7, 3, 4], [9, 1, 10]])

a_inv=np.linalg.inv(a1)
a_rk = np.linalg.matrix_rank(a1)
a_det=np.linalg.det(a1)
a_eig=np.linalg.eig(a1)

print('Inverse = \n', a_inv)
print('\nRank = \n', a_rk)
print('\nDeterminant = \n', a_det)
print('\nEigenvalues = \n', a_eig)