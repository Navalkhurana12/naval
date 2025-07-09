import numpy as np

# 1D array
a = np.array([10, 20, 30,34,56,3])

# 2D array
b = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])


c=b.ravel()
d=a+c
print(d)
print("question no 2")
import numpy as np
h=np.array([[12,34,5],[45,76,43]])
k=h.flatten()
print(k)
print("question 3")
ar=np.array([1,2,34,5,6,7])
print(np.flip(ar))
print("question 4")
n1=np.array([21,3,2,4,2])
n2=np.array([67,43,5,4,3])
print(np.max(n1))
print(np.min(n1))
print(n1.shape)
b=n1[2:4]
print(b)
y=np.array([[23,43,43,23,2],[54,45,65,54,7]])
sum=0
for x in np.nditer(y):
    sum+=x
print(sum)
print(n1-n2)
print(n1+n2)
print(n1/n2)
print(n1*n2)