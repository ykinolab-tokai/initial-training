# (1) a=[4, 8, 3, 4, 1] というリストに対し、要素が偶数なら 0, 奇数なら 1 に変換するコード
a = [4, 8, 3, 4, 1]
change_list = [0 if x % 2 == 0 else 1 for x in a]
print(change_list) 

# (2) (1)のコードを組み込み関数を使って奇数の個数を数えるコード
count_list = sum([1 for x in a if x % 2 != 0])
print(count_list)  

# (3) リスト a から奇数の要素だけを残すコード
odd_list = [x for x in a if x % 2 != 0]
print(odd_list) 
