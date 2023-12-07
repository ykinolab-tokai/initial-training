a=[4, 8, 3, 4, 1]
b = []
for n in a:
  b.append(n%2)
print(b)
print(b.count(1))

hensu = [x for x in a if x % 2]
print(hensu)

