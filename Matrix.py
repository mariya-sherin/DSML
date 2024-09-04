import numpy as np

a1=np.array([[2,2,4],[7,1,2],[6,7,8]])
a2=np.array([[1,2,3],[4,5,6],[2,8,4]])

print('Addition')
print(np.add(a1,a2))

print('Subtraction')
print(np.subtract(a1,a2))

print('Product')
print(np.multiply(a1,a2))

print('Division')
print(np.divide(a1,a2))

print('Transpose of matrix 1')
print(a1.T)

print('Transpose of matrix 2')
print(a2.T)

print('Sum of diagonal elements of matrix 1')
print(sum(np.diag(a1)))

print('Sum of diagonal elements of matrix 2')
print(sum(np.diag(a2)))