import numpy as np

# 5×4行列を作成（例として1から始まる連番の値を使用）
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16],
                   [17, 18, 19, 20]])

# 5×4行列の要素を表示
print("5×4行列の要素:")
print(matrix)

# 2行3列の要素を取得
element_2_3 = matrix[1, 2]
print("\n2行3列の要素:")
print(element_2_3)

# 第2列の要素を取得
column_2 = matrix[:, 1]
print("\n第2列の要素:")
print(column_2)

# 奇数番目の行の要素を取得
odd_rows = matrix[::2, :]
print("\n奇数番目の行の要素:")
print(odd_rows)