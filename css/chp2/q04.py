a = [4, 8, 3, 4, 1]
squares = [x ** 2 for x in a]
print(squares)

a = [4, 8, 3, 4, 1]
result = [0 if x % 2 == 0 else 1 for x in a]
print(result)

x = sum(1 for x in a if x % 2 != 0)
print(x)
