import numpy as np
import matplotlib.pyplot as plt

# Define parameters

Q = 3  # Replace with your desired value
C = 2 # Replace with your desired value
 # Replace with your desired value
R = .8
Q_0=.75
X1=.1
d=2

# Create a grid of points
x = np.linspace(-3, 3, 100)  # Avoid division by zero at (0, 0)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Calculate ϕ and ψ
s= -Q_0 * (- ((X+d) * R ** 2) / ((X+d) ** 2 + Y ** 2))-(Q / (4 * np.pi)) * np.log(((X+d)**2 + Y**2)/R**2)
m= -Q_0 * ((Y * R ** 2) / ((X+d) ** 2 + Y ** 2))-(Q / (2 * np.pi)) * np.arctan2(Y, X+d) 
phi = -Q_0 * ((X) - ((X-d) * R ** 2) / ((X-d) ** 2 + Y ** 2))+(Q / (4 * np.pi)) * np.log(((X-d)**2 + Y**2)/R**2) +s+ C
psi = -Q_0 * (Y + (Y * R ** 2) / ((X-d) ** 2 + Y ** 2))+(Q / (2 * np.pi)) * np.arctan2(Y, X-d)+m 

# Create a single plot for both ϕ and ψ
plt.figure(figsize=(8, 6))
contour1 = plt.contour(X, Y, phi, levels=45, colors='black', linestyles='dashed')
contour2 = plt.contour(X, Y, psi, levels=45, colors='blue', linestyles='solid')

plt.xlabel('x')
plt.ylabel('y')
plt.title('A circular Lake in uniform flow field with net inflow')
# plt.savefig("A circular Lake in uniform flow field with net inflow and river as boundary.png")
plt.show()