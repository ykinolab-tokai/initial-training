import numpy as np

array = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                    [17, 18, 19, 20]])
val = array[1,2]
print("2行3列の要素:",val)

column_1 = array[:,1]
print("第2列の要素すべて:",column_1)

row_1 = array[::2,:]
print("奇数番目の行の要素すべて:",row_1)
