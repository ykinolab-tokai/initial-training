import numpy as np
import matplotlib.pyplot as plt

# xの範囲を設定
x_values = np.linspace(0.01, 5, 100)

# 関数の定義
y_log = np.log(x_values)
y_log2 = np.log2(x_values)
y_log10 = np.log10(x_values)

# グラフをプロット
plt.figure(figsize=(8, 6))

plt.plot(x_values, y_log, label='$\log(x)$')
plt.plot(x_values, y_log2, label='$\log_2(x)$')
plt.plot(x_values, y_log10, label='$\log_{10}(x)$')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of Logarithmic Functions')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# グラフを保存
plt.plot(x, y) # 散布図グラフを描画
plt.savefig("scatter.png")