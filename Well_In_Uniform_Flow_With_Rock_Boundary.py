import numpy as np
import matplotlib.pyplot as plt

# Define parameters

Q = .2  # Replace with your desired value
C = 10 # Replace with your desired value
d = .1 # Replace with your desired value

# Create a grid of points
x = np.linspace(-.4, .4, 500)  # Avoid division by zero at (0, 0)
y = np.linspace(-.4, .4, 500)
X, Y = np.meshgrid(x, y)

# Calculate ϕ and ψ
r1 = np.sqrt((X+d)**2 + Y**2)
r2 = np.sqrt((X-d)**2+Y**2)
s1= np.arctan2(Y, X+d)
s2=np.arctan2(Y, X-d)
phi = (Q / (2 * np.pi)) * np.log(r1*r2) + C
psi = (Q / (2 * np.pi)) * (s1+s2) 

# Create a single plot for both ϕ and ψ
plt.figure(figsize=(8, 6))
contour1 = plt.contour(X, Y, phi, levels=20, colors='black', linestyles='dashed')
contour2 = plt.contour(X, Y, psi, levels=20, colors='blue', linestyles='solid')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour of a Well with Rock as Boundary')
plt.savefig("well_in_Rock_as_Boundary.png")
plt.show()
