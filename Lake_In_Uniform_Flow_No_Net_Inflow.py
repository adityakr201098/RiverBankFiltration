import numpy as np
import matplotlib.pyplot as plt

# Define parameters
Q_0 =.5  # Replace with your desired value
C = .01  # Replace with your desired value
R = .1

# Create a grid of points
x = np.linspace(-0.5, 0.5, 60)  # Avoid division by zero at (0, 0)
y = np.linspace(-0.5, 0.5, 60)
X, Y = np.meshgrid(x, y)

# Calculate ϕ and ψ for each point on the grid
phi = -Q_0 * (X - (X * R ** 2) / (X ** 2 + Y ** 2)) + C
psi = -Q_0 * (Y + (Y * R ** 2) / (X ** 2 + Y ** 2))

# Create a single plot for both ϕ and ψ
plt.figure(figsize=(8, 6))
contour1 = plt.contour(X, Y, phi, levels=20, colors='black', linestyles='dashed')
contour2 = plt.contour(X, Y, psi, levels=20, colors='blue', linestyles='solid')

plt.xlabel('x')
plt.ylabel('y')
plt.title('A circular Lake in uniform flow field with no net flow')
# plt.savefig("A circular Lake in uniform flow field with no net flow.png")
plt.show()
