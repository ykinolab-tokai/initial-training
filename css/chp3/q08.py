import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.1,5,50)

y_log=np.log(x)
y_log2=np.log2(x)
y_log10=np.log10(x)

plt.plot(x, y_log)
plt.plot(x, y_log2)
plt.plot(x, y_log10)

plt.show()
