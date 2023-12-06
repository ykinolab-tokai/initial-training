import numpy as np

a = np.array([[1 ,2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])
print(a)
print()

b = a[2, 3]
print(b)
print()

c = a[2, 0:3]
print(c)
print()

d = a[1::2,]
print(d)
print()