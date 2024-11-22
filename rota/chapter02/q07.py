def f(a):
    a = [6, 7, 8]

def g(a):
    a.append(1)

def somefunction():
    a0 = [1, 2, 3]
    f(a0)
    print(a0)

    a1 = [1, 2, 3]
    g(a1)
    print(a1)

somefunction()

# 考察
# fという関数にaを代入して[6,7,8]になっている所を，a0に変えただけではそのまま置き換わるだけである
# リストに1が追加されるのはappendがリスト自体を変更するから