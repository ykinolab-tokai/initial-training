import math  # exp を呼び出すために math モジュールをインポート

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

def g(x):
    return math.log(x)

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

for i in range(-3, 4):
    print(i)
    print(f(i))
    print(dfdx_approx(i))
    print()

print('--------------------')
print()

for j in range(-2, 4):
    print(2**j)
    print(g(2**j))
    print(dgdx_approx(2**j))
    print()

    