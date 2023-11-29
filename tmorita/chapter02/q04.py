a = [4, 8, 3, 4, 1]
result = [0 if x % 2 == 0 else 1 for x in a]
print(result)

a = [4, 8, 3, 4, 1]
count_odd = sum(1 for x in a if x % 2 != 0)
print(count_odd)

a = [4, 8, 3, 4, 1]
filtered_list = [x for x in a if x % 2 != 0]
print(filtered_list)


