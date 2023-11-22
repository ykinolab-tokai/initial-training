import numpy as np

x = np.arange(0, 361, 1)

sin_1 = np.sin(np.radians(x))
sin_1 = np.round(sin_1, 3)
cos_1 = np.cos(np.radians(x))
cos_1 = np.round(cos_1, 3)
tan_1 = np.tan(np.radians(x))
tan_1 = np.round(tan_1, 3)

print("角度\t正弦\t余弦\t正接")

for x, sin_x, cos_x, tan_x in zip(x, sin_1, cos_1, tan_1):
    print(f"{x}°\t{sin_x}\t{cos_x}\t{tan_x}")
