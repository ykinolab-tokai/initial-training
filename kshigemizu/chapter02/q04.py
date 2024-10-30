a = [4, 8, 3, 4, 1]
b = [i%2 for i in a]
print(b)


b = [i%2 for i in a]
res = sum(b)
print(res)

b = [i for i in a if i%2]
print(b)