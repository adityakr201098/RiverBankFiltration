from scipy.optimize import minimize_scalar

def Gp(X, Y, X0, Y0, R):
    condition = (X - X0)**2 + (Y - Y0)**2 < R**2
    result = np.where(condition, -0.25 * ((X - X0)**2 + (Y - Y0)**2 - R**2),
                      -((R**2)/4) * np.log(((X - X0)**2 + (Y - Y0)**2) / R**2))
    return result

def phi(X, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0):
    term1 = (Q / (4 * np.pi)) * np.log(((X - Xw)**2 + (Y - Yw)**2) / ((X + Xw)**2 + (Y + Yw)**2))
    term2 = Q_0 * X
    term3 = -0.00005 * (Gp(X, Y, X0, Y0, R) + ((R**2)/4) * np.log(((X - X0)**2 + (Y - Y0)**2) / R**2))
    return term1 + term2 + term3 + phi_0

def dphi_dX(X, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0):
    epsilon = 1e-6  # Small epsilon value for numerical differentiation
    dphi_X = (phi(X + epsilon, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0) - phi(X - epsilon, Y, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0)) / (2 * epsilon)
    return dphi_X

# Define the parameters
Xw = 100
Yw = 0
Q = 0.013888
Q_0 = 0.00005787 
X0 = 200
Y0 = 0
R = 25
phi_0 = 0.2314

# Define a function to find the absolute value of the derivative of phi with respect to X
def abs_dphi_dX(X, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0):
    return abs(dphi_dX(X, 0, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0))

# Use minimize_scalar to find the minimum of abs_dphi_dX, which corresponds to where the derivative with respect to X is closest to 0
res = minimize_scalar(abs_dphi_dX, args=(Xw, Yw, Q, Q_0, X0, Y0, R, phi_0), bounds=(0, X0))

# The result will be in res.x
X_solution = res.x
Y_solution = phi(X_solution, 0, Xw, Yw, Q, Q_0, X0, Y0, R, phi_0)
print("Solution for X:", X_solution)
print("Solution for Y:", Y_solution)
