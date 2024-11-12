import math

def f(x):
    return math.exp(x)

def dfdx_exact(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

# 与えられた点での数値微分と正確な微分の比較
x_values = [-3, -2, -1, 0, 1, 2, 3]

for x in x_values:
    approx_derivative = dfdx_approx(x)
    exact_derivative = dfdx_exact(x)
    
    print(f"x = {x}: 数値微分の結果 = {approx_derivative}, 正確な微分の値 = {exact_derivative}, 誤差 = {abs(approx_derivative - exact_derivative)}")

import math

def g(x):
    return math.log(x)

def dldx_exact(x):
    return 1 / x

def dldx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

# 与えられた点での数値微分と正確な微分の比較
x_values_log = [0.25, 0.5, 1, 2, 4, 8]

for x in x_values_log:
    approx_derivative = dldx_approx(x)
    exact_derivative = dldx_exact(x)
    
    print(f"x = {x}: 数値微分の結果 = {approx_derivative}, 正確な微分の値 = {exact_derivative}, 誤差 = {abs(approx_derivative - exact_derivative)}")