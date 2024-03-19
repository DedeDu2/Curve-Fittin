import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Example data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 2, 4, 6, 8, 10])

# Define a model function
def linear_model(x, m, c):
    return m * x + c

# Fit the model to the data
params, covariance = curve_fit(linear_model, x_data, y_data)

# Plot the data and fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, linear_model(x_data, *params), color='red', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting: Linear Model')
plt.legend()
plt.grid(True)
plt.show()
