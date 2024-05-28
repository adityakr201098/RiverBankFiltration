import numpy as np
import matplotlib.pyplot as plt

# Define parameters
Q_0 = 1  # Replace with your desired value
Q = 1  # Replace with your desired value
C = 10  # Replace with your desired value

# Create a grid of points
Nx = 200  # You need to define Nx and Ny
Ny = 200
x = np.linspace(-0.5, 0.5, Nx)
y = np.linspace(-0.5, 0.5, Ny)
X, Y = np.meshgrid(x, y)
phi = np.zeros((Ny, Nx))
psi = np.zeros((Ny, Nx))

# Calculate ϕ and ψ
for i in range(Nx):
    for j in range(Ny):
        r = np.sqrt(X[j, i]**2 + Y[j, i]**2)
        phi[i, j] = -Q_0 *X[i,j] + (Q / (2 * np.pi)) * np.log(r) + C
        psi[i, j] = -Q_0 * Y[i, j] + (Q / (2 * np.pi)) * np.arctan2(Y[i, j], X[i,j]) + C

# Create a single plot for both ϕ and ψ
plt.figure(figsize=(8, 6))
contour1 = plt.contour(X, Y, phi, levels=20, colors='blue', linestyles='dashed')
contour2 = plt.contour(X, Y, psi, levels=20, colors='g')

# Add a legend


plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour plot of ϕ and ψ')

plt.show()
