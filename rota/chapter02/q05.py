# (1) str.join() を使って、0 から 99 までの数をスペース区切りで並べた文字列を構成
string = " ".join([str(i) for i in range(100)])
print(string) 

# (2) str.format() を使って float の値 (1.0 / 7.0) の小数点以下9桁までを表示
value = 1.0 / 7.0
format_value = "{:.9f}".format(value)
print(format_value) 