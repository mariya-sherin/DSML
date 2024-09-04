#write a program to display elements of the matrix 'X' to different powers. Also display the identity matrix
import numpy as np
X = np.array([[1,2],[3,4]])
print('display each element of the matrix to different powers',np.power(X,[[1,2],[3,4]]))

identity_matrix = np.identity(X.shape[0])
print("\nIdentity matrix of the same shape as X:")
print(identity_matrix)