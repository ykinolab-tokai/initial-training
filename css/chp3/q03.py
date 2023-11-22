import numpy as np

array_zeros = np.zeros((3, 3))
print("すべての要素が0:")
print(array_zeros)

array_zeros = np.zeros((3, 3))
print("すべての要素が1:")
print(array_zeros)

array_random = np.random.uniform(-1, 1, (3, 3))
print("-1から1の間のランダムな要素:")
print(array_random)

array_diagonal = np.eye(3) * 2
print("対角の要素が2で，他の要素が0:")
print(array_diagonal)
