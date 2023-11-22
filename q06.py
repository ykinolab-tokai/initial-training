import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)

def function_1(x):
    return x**3 - 6*x**2 + 9*x - 3

def function_2(x):
    return function_1(x + 2) + 2
plt.plot(x,function_1(x))
plt.plot(x,function_2(x))
plt.show()
