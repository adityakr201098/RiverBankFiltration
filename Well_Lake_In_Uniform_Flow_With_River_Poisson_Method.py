import numpy as np
import matplotlib.pyplot as plt

def Gp(X, Y, X0, Y0, R):
    condition = (X - X0)**2 + (Y - Y0)**2 < R**2
    result = np.where(condition, -0.25 * ((X - X0)**2 + (Y - Y0)**2 - R**2),
                      -((R**2)/4) * np.log(((X - X0)**2 + (Y - Y0)**2) / R**2))
    return result


def phi(X, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0):
    term1 = (Q / (4 * np.pi)) * np.log(((X - Xw)**2 + (Y - Yw)**2) / ((X + Xw)**2 + (Y - Yw)**2))
    term2 = Q_0 * X
    term3 = (5/np.pi*R**2)*(Gp(X, Y, X0, Y0, R) +((R**2)/4) * np.log(((X - X0)**2 + (Y - Y0)**2) / R**2))
    return term1 + term2 + term3 + phi_0

# Define the grid for X and Y
X = np.linspace(0, 600, 1000)
Y = np.linspace(-250, 250, 1000)
X, Y = np.meshgrid(X, Y)

# Set parameters
Xw, Yw = 100,0  # Adjust as needed
Q, Q_0 = 0.0006, 0.00000115   # Adjust as needed
X0, Y0, R = 300, 0, 50 # Adjust as needed
phi_0 = 0.005  #djust as needed

# Calculate phi values for the grid
phi_values = phi(X, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0)
# phi_values = np.abs(phi_values)


K=0.00011
# B=20
# H = (phi_values+ 0.5*K*B**2)/(K*B)
# phi_values = np.nan_to_num(phi_values)
H = np.sqrt((2 * phi_values) / K)
# Create a single plot for both ϕ and ψ
plt.figure(figsize=(8, 6))

# Contour plot for head (H)
contour1 = plt.contourf(X, Y, H, levels=20, cmap='winter', alpha=0.75)

# Add colorbar for the stream function
cbar = plt.colorbar(contour1)
cbar.set_label('Head(m)')

# Stream plot for vector field (U, V)
U = -np.gradient(phi_values, axis=1)
V = -np.gradient(phi_values, axis=0)
streamplot = plt.streamplot(X, Y, U, V, color='blue', linewidth=0.5, arrowsize=1, arrowstyle='->')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Head and Streamplot')
plt.savefig('poisson4')
plt.show()


