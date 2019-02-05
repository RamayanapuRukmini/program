import numpy
m=input("enter first matrix rows")
n=input("enter first matrix columns")
array=[[0 for j in range(0,n)]for i in range(0,m)]
print("enter  matrix values:")
for i in range(0,m):
	for j in range(0,n):
		array[i][j]=input("enter element")
print("matrix:")
print(array)
inverse=numpy.linalg.inv(array)
print("inverse of a matrix:")
print(inverse)
