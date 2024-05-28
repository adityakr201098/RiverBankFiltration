import numpy as np
import matplotlib.pyplot as plt

def Gp(X, Y, X0, Y0, R):
    condition = (X - X0)**2 + (Y - Y0)**2 < R**2
    result = np.where(condition, -0.25 * ((X - X0)**2 + (Y - Y0)**2 - R**2),
                      -((R**2)/4) * np.log(((X - X0)**2 + (Y - Y0)**2) / R**2))
    return result


def phi(X, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0):
    term1 = (Q / (4 * np.pi)) * np.log(((X - Xw)**2 + (Y - Yw)**2) / ((X + Xw)**2 + (Y + Yw)**2))
    term2 = Q_0 * X
    term3 = -.00005*(Gp(X, Y, X0, Y0, R) +((R**2)/4) * np.log(((X - X0)**2 + (Y - Y0)**2) / R**2))
    return term1 + term2 + term3 + phi_0

# Define the grid for X and Y
X = np.linspace(0, 600, 1000)
Y = np.linspace(-200, 200, 1000)
X, Y = np.meshgrid(X, Y)

# Set parameters
Xw, Yw = 100, 0  # Adjust as needed
Q, Q_0 = 0.013888, 0.00005787   # Adjust as needed
X0, Y0, R = 200, 0, 25 # Adjust as needed
phi_0 = 0.2314  #djust as needed

# Calculate phi values for the grid
phi_values = phi(X, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0)

K=0.001157

H = np.sqrt((2 * phi_values) / K)

plt.figure(figsize=(8, 6))
contour_H = plt.contour(X, Y,H, levels=45, colors='black', linestyles='solid')
plt.clabel(contour_H, inline=True, fontsize=10, fmt='%1.2f')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour of head')
# plt.savefig('Contour of head in poisson11')
plt.show()