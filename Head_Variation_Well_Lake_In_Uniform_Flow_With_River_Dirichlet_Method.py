import numpy as np
import matplotlib.pyplot as plt

# Define parameters
Q_0 = 0.00005787
C = 0.2314  # River phi
R = 25
Q1 = 0.013888  # WELL
Q = 0.05906 # LAKE
Xw = 100
m = 0
d = 200
phi=0.267411
j=20
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
# H = (phi+0.5*K*j**2)/(K*j)

plt.figure(figsize=(8, 6))
contour_H = plt.contour(X, Y,H, levels=25, colors='black', linestyles='solid')
plt.clabel(contour_H, inline=True, fontsize=12, fmt='%1.2f')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour of head')
# plt.savefig('Contour of head8')
plt.show()
