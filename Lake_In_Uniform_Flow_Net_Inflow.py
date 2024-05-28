import numpy as np
import matplotlib.pyplot as plt

# Define parameters

Q = 4.9  # Replace with your desired value
C = 1.0 # Replace with your desired value
 # Replace with your desired value
R = .7
Q_0=.7
X1=.1

# Create a grid of points
x = np.linspace(-5, 5, 200)  # Avoid division by zero at (0, 0)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Calculate ϕ and ψ

phi = -Q_0 * (X - (X * R ** 2) / (X ** 2 + Y ** 2))+(Q / (4 * np.pi)) * np.log((X**2 + Y**2)/R**2) + C
psi = -Q_0 * (Y + (Y * R ** 2) / (X ** 2 + Y ** 2))+(Q / (2 * np.pi)) * np.arctan2(Y, X) 

# Create a single plot for both ϕ and ψ
plt.figure(figsize=(8, 6))
contour1 = plt.contour(X, Y, phi, levels=20, colors='black', linestyles='dashed')
contour2 = plt.contour(X, Y, psi, levels=20, colors='blue', linestyles='solid')

plt.xlabel('x')
plt.ylabel('y')
plt.title('A circular Lake in uniform flow field with net inflow')
# plt.savefig("A circular Lake in uniform flow field with net inflow.png")
plt.show()