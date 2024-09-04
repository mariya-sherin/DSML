#Write a Program to display various elements of a given 4x4 matrix  specifying appropriate indices

import numpy as np
a=np.array([[7,3,2,1],[5,6,7,8],[9,3,2,1],[4,1,2,6]])
print(a)
print("excluding first row")
print(a[1:,:])

print("excluding last column")
print(a[:,:-1])

print("elements of first and second columns in 2nd and 3rd row ")
print(a[1:3,:2])

print("elements of 2nd and third columns")
print(a[:,1:3])

print("second and third element of first row")
print(a[:1,1:3])

print("elements from indices 4 to 10 in descending order")
a_new=a.reshape(1,-1)[0][4:11]
print(-np.sort(-a_new))

