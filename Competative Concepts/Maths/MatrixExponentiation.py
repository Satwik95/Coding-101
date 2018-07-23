from numpy import linalg as LA
import numpy as np

f1 = []
print("Enter K")
k = int(input())
print("enter the f1 values")
for i in range(0,k):
    x = input()
    f1.append(int(x))

coef = []
print("Enter the coef")
for i in range(0,k):
    x = input()
    coef.append(int(x))

# form T matrix
T = np.zeros((k,k))

for i in range(0,k):
    for j in range(0,k):
        if i<k and i!=k-1:
            if j==i+1:
                T[i][j] = 1
            continue
        T[i][j] = coef[k-j-1]
        
# find T^n-1
print("Please enter the nth value")
n=int(input())
T_n = np.asmatrix(LA.matrix_power(T, n-1))
f1 = np.asmatrix(f1)
res = np.matmul(T_n,np.transpose(f1))
res = np.asarray(res).reshape(-1)
           
print("The f(n) = " + str(res[0]))
