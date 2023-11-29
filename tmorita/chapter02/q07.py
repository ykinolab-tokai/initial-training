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

f関数内での変更が影響しないため、元のリストが表示される。
g関数内での変更が影響し、元のリストに要素1が追加されたリストが表示された。


