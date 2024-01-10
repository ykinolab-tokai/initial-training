import math

def num_d(func, x, delta_h=0.0001):
    return (func(x + delta_h) - func(x)) / delta_h

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh
# (1) 指数関数 exp(x) の数値微分
def exp1(x):
    return math.exp(x)

x_exp = [-3, -2, -1, 0, 1, 2, 3]


for x in x_exp:
    num_result = num_d(exp1, x)
    exact_result = exp1(x)
    print(f"At x={x}: Numerical = {num_result}, Exact = {exact_result}")

# (2) 対数関数 log(x) の数値微分
def log1(x):
    return math.log(x)

x_log = [0.25, 0.5, 1, 2, 4, 8]


for x in x_log:
    num_result = num_d(log1, x)
    exact_result = 1 / x  
    print(f"At x={x}: Numerical = {num_result}, Exact = {exact_result}")




