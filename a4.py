import numpy as np
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

C=[[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
print("Addition using List:")
print(C)

A=np.array(A)
B=np.array(B)
C=A+B

print("Addition using NumPy:")
print(C)