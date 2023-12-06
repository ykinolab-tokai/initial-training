import numpy as np
import matplotlib.pyplot as plt

# 関数の定義
def original_function(x):
    return x**3 - 6*x**2 + 9*x - 3

# xの範囲を設定
x_values = np.linspace(-5, 5, 100)

# グラフをプロット
plt.figure(figsize=(8, 6))

# オリジナルの関数をプロット
plt.plot(x_values, original_function(x_values), label='Original Function')

# 平行移動後の関数をプロット
shifted_function = original_function(x_values) - 2  # x軸方向に-2平行移動
plt.plot(x_values, shifted_function, label='Shifted Function')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of $y=x^3-6x^2+9x-3$ and Shifted Function')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# グラフを保存

plt.plot(x, y) # 散布図グラフを描画
plt.savefig("scatter.png")