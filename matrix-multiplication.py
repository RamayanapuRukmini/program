m=input("enter first matrix rows")
n=input("enter first matrix columns")
p=input("enter second matrix rows")
q=input("enter second matrix columns")
if (n!=p):
  print("matrix mult not exist")
  exit();
array1=[[0 for j in range(0,n)]for i in range(0,m)]
array2=[[0 for j in range(0,q)]for i in range(0,p)]
output=[[0 for j in range(0,q)]for i in range(0,m)]
print("enter first matrix values:")
for i in range(0,m):
	for j in range(0,n):
		array1[i][j]=input("enter element")
print("enter second matrix elements")
for i in range(0,p):
	for j in range(0,q):
		array2[i][j]=input("enter element")
print("first matrix");
print(array1)
print("second matrix");
print(array2)


for i in range(0,m):
	for j in range(0,q):
		for k in range(0,n):
			output[i][j]+=array1[i][k]*array2[k][j]
print("mult of two matrices")
print(output)


