import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 100)

y1 = np.log(x)
y2 = np.log2(x)
y3 = np.log10(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()