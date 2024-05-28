import numpy as np
import matplotlib.pyplot as plt

# Define parameters
Q_0 = 0.00005787
C = 0.2314  # TARGET phi
R = 25
Q1 = 0.013888  # WELL
Q = 0.0057  # LAKE
Xw = 100
m = 0
d = 200

K = 0.001157

# Create points along the circumference
theta = np.linspace(0, 2 * np.pi, 1000)
X = d + R * np.cos(theta)
Y = m + R * np.sin(theta)

# Calculate phi_1 for each point
Z1 = (Q1 / (4 * np.pi)) * np.log((((X + Xw - d) ** 2 + (Y - m) ** 2) * (R ** 2)) / (((X + ((R ** 2) / Xw) - d) ** 2) + ((Y - m) ** 2) * Xw ** 2))

phi_1 = Q_0 * (X - (((X - d) * R ** 2) / ((X - d) ** 2 + (Y - m) ** 2))) - (Q / (4 * np.pi)) * np.log((((X - d) ** 2) + ((Y - m) ** 2)) / (R ** 2)) +Z1 + C

Z2 = (Q1 / (4 * np.pi)) * np.log((((X - Xw + d) ** 2 + (Y - m) ** 2) * (R ** 2)) / (((X - ((R ** 2) / Xw) + d) ** 2) + ((Y - m) ** 2) * Xw ** 2))

phi_2 = Q_0* (X - (((X + d) * R ** 2) / ((X + d) ** 2 + (Y - m) ** 2))) + (Q / (4 * np.pi)) * np.log((((X + d) ** 2) + ((Y - m) ** 2)) / (R ** 2)) - Z2 

phi = phi_1+phi_2
H = np.sqrt((2 * phi) / K)
# Plotting
plt.plot(theta, H)
plt.xlabel('Theta')
plt.ylabel('H')
plt.title('Head along circumference of lake')
plt.grid(False)
# plt.savefig('L+U+W+R6.png')
plt.show()
