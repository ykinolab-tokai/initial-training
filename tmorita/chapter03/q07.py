import numpy as np
import matplotlib.pyplot as plt

# xの範囲を設定
x_values = np.linspace(-2, 2, 100)

# 関数の定義
y1 = 2 ** x_values
y2 = 2 ** (-x_values)

# グラフをプロット
plt.figure(figsize=(8, 6))

plt.plot(x_values, y1, label='$y = 2^x$')
plt.plot(x_values, y2, label='$y = 2^{-x}$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of $y = 2^x$ and $y = 2^{-x}$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# グラフを保存
plt.plot(x, y) # 散布図グラフを描画
plt.savefig("scatter.png")