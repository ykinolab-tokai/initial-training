import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)

y1 = 2 ** x
y2 = 2 ** (-x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()