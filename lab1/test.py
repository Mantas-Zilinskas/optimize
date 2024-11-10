import numpy as np
import matplotlib.pyplot as plt

# Define the function
def func(x, a=2, b=1):
    return (x**2 - b)**2 / (a - 1)

# Generate x values
x = np.linspace(-3, 3, 400)
y = func(x)

# Define the range between which to fill (e.g., between x = -2 and x = 2)
x_fill_start = -2
x_fill_end = 2

# Create the mask to fill only between x_fill_start and x_fill_end
mask = (x >= x_fill_start) & (x <= x_fill_end)

# Plot the function
plt.plot(x, y, label="f(x) = (x^2 - b)^2 / (a - 1)")

# Fill the area below the curve and the x-axis
#plt.fill_between(x[mask], y[mask], color='blue', alpha=0.3, label='Area under curve')

# Fill the area above the curve
#plt.fill_between(x[mask], y[mask], y2=max(y), color='red', alpha=0.2, label='Area above curve')
plt.fill_between([1,3], [0 , 0], y2=max(y), color='red', alpha=0.2, label='Area above curve')
plt.fill_between([-1,0], [0 , 0], y2=9999999, color='red', alpha=0.2, label='Area above curve')
# Add labels and title
plt.title('Filling Areas Above and Below the Curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()