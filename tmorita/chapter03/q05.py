import numpy as np

# 0度から360度まで1度刻みの角度の配列を作成
angles = np.arange(0, 361, 1)

# 角度をラジアンに変換
angles_rad = np.radians(angles)

# 三角関数の値を計算
sin_values = np.sin(angles_rad)
cos_values = np.cos(angles_rad)
tan_values = np.tan(angles_rad)

# 三角関数表を表示
print("角度 |  sin(θ)  |  cos(θ)  |  tan(θ)")
print("-" * 35)
for angle, sin_val, cos_val, tan_val in zip(angles, sin_values, cos_values, tan_values):
    print(f"{angle:3d}° | {sin_val:.4f} | {cos_val:.4f} | {tan_val:.4f}")