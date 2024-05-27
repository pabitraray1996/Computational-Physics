import numpy as np
import matplotlib.pyplot as plt

# Load the exponential random numbers from the file
exp_numbers = np.loadtxt('exp_numbers.txt')

f= plt.figure()
# Plot the density histogram
plt.hist(exp_numbers, bins=100, density=True, alpha=0.6, color='g', label='Histogram')

# Plot the exponential PDF for comparison
x = np.linspace(0, max(exp_numbers), 1000)
lambda_ = 2.0  # Mean = 0.5, so lambda = 2
exp_pdf = lambda_ * np.exp(-lambda_ * x)
plt.plot(x, exp_pdf, 'r-', lw=2, label='Exponential PDF')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Exponential Random Numbers vs. Exponential PDF')
plt.legend()
plt.show()

f.savefig('Figure_4.pdf',bbox_inches='tight')