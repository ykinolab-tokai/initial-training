import numpy as np
import matplotlib.pyplot as plt

a = 1
b = -6
c = 9
d = -3

x = np.linspace(-5, 5, 100)
y = a * x**3 + b * x**2 + c * x + d

plt.plot(x, y)
plt.show()

y = a * (x + 2)**3 + b * (x + 2)**2 + c * (x + 2) + d + 2
plt.plot(x, y)
plt.show()
