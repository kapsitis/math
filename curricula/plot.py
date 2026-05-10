import numpy as np
import matplotlib.pyplot as plt

# ---- Curve from: x^2 + (y - cbrt(x^2))^2 = 1
# Solve for y:
# (y - cbrt(x^2))^2 = 1 - x^2  =>  y = cbrt(x^2) ± sqrt(1 - x^2)
x = np.linspace(-1, 1, 3000)
c = np.cbrt(x**2)
s = np.sqrt(np.maximum(0.0, 1 - x**2))
y_plus  = c + s
y_minus = c - s

# ---- Plot setup
fig, ax = plt.subplots(figsize=(7, 7))

# Limits (chosen to nicely frame the curve)
xlim = (-1.5, 1.5)
ylim = (-1.5, 1.8)
ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_aspect("equal", adjustable="box")

# ---- Custom grid: step 0.1 (light gray), thicker at multiples of 0.5 and 1.0
def is_multiple(val, step, tol=1e-9):
    return abs(val/step - round(val/step)) < tol

grid_step = 0.1
xs = np.arange(np.floor(xlim[0]/grid_step)*grid_step, xlim[1] + grid_step/2, grid_step)
ys = np.arange(np.floor(ylim[0]/grid_step)*grid_step, ylim[1] + grid_step/2, grid_step)

for xv in xs:
    lw = 0.6
    if is_multiple(xv, 1.0):
        lw = 1.4
    elif is_multiple(xv, 0.5):
        lw = 1.0
    ax.axvline(xv, color="#d3d3d3", linewidth=lw, zorder=0)

for yv in ys:
    lw = 0.6
    if is_multiple(yv, 1.0):
        lw = 1.4
    elif is_multiple(yv, 0.5):
        lw = 1.0
    ax.axhline(yv, color="#d3d3d3", linewidth=lw, zorder=0)

# ---- Axes lines
ax.axhline(0, color="black", linewidth=1.2)
ax.axvline(0, color="black", linewidth=1.2)

# ---- Axis ticks/labels: step 0.5 on both axes
tick_step = 0.5
xticks = np.arange(np.ceil(xlim[0]/tick_step)*tick_step, xlim[1] + 1e-12, tick_step)
yticks = np.arange(np.ceil(ylim[0]/tick_step)*tick_step, ylim[1] + 1e-12, tick_step)
ax.set_xticks(xticks)
ax.set_yticks(yticks)

# ---- Plot the curve in dark red
curve_color = "#8B0000"  # dark red
ax.plot(x, y_plus,  color=curve_color, linewidth=2.5)
ax.plot(x, y_minus, color=curve_color, linewidth=2.5)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"$x^2 + \left(y - \sqrt[3]{x^2}\right)^2 = 1$")

plt.show()