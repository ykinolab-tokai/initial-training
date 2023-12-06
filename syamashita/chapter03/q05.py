import numpy as np

degrees = np.arange(0, 4, 1)
radians = np.radians(degrees)

sin_values = np.sin(radians)
cos_values = np.cos(radians)
tan_values = np.tan(radians)


tring_table = np.array([degrees, sin_values, cos_values, tan_values]).T
print(tring_table)