import numpy as np
import matplotlib.pyplot as plt

# Define parameters
Q_0 = 0.00005787
C = 0.2314  # TARGET phi
R = 25
Q1 = 0.1388  # WELL
Q = 0.08906  # LAKE
Xw = 100
m = 0
d = 200

K = 0.001157

# Create points along the circumference
x = np.linspace(0, 600, 1000)
y = np.linspace(-200, 200, 1000)
X, Y = np.meshgrid(x, y)

# Calculate phi_1 for each point
Z1 = (Q1 / (4 * np.pi)) * np.log((((X - Xw) ** 2) + ((Y - m) ** 2)) / (R ** 2))

phi_1 = Q_0 * (X - (((X - d) * R ** 2) / ((X - d) ** 2 + (Y - m) ** 2))) - (Q / (4 * np.pi)) * np.log((((X - d) ** 2) + ((Y - m) ** 2)) / (R ** 2)) + Z1 + C

Z2 = (Q1 / (4 * np.pi)) * np.log((((X + Xw) ** 2) + ((Y + m) ** 2)) / (R ** 2))

phi_2 = Q_0 * (0- (((X + d) * R ** 2) / ((X + d) ** 2 + (Y - m) ** 2))) + (Q / (4 * np.pi)) * np.log((((X + d) ** 2) + ((Y - m) ** 2)) / (R ** 2)) - Z2

phi = phi_1 + phi_2

H = np.sqrt((2 * phi) / K)


plt.figure(figsize=(8, 6))
# contour_H = plt.contour(X, Y,H, levels=50, colors='black', linestyles='solid')
# plt.clabel(contour_H, inline=True, fontsize=10, fmt='%1.2f')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Contour of head')
# plt.savefig('Contour of head3')
# plt.show()
contour1 = plt.contourf(X, Y, H, levels=20, cmap='winter', alpha=0.7)
cbar = plt.colorbar(contour1)
cbar.set_label('Head(m)')

# Stream plot for vector field (U, V)
U = -np.gradient(phi, axis=1)
V = -np.gradient(phi, axis=0)
streamplot = plt.streamplot(X, Y, U, V, color='blue', linewidth=0.5, arrowsize=1, arrowstyle='->')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Head and Stream Plot')
plt.savefig('Head and Stream Plot112')
plt.show()