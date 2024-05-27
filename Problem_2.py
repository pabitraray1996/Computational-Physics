import numpy as np
import matplotlib.pyplot as plt

# Generate 10,000 random numbers using np.random.rand()
n_samples = 10000
random_numbers = np.random.rand(n_samples)

f= plt.figure()
# Plot the density histogram
plt.hist(random_numbers, bins=100, density=True, alpha=0.6, color='g')

# Plot the uniform PDF for comparison
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)
plt.plot(x, uniform_pdf, 'r-', lw=2)

# Labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of np.random.rand() Numbers vs. Uniform PDF')
plt.show()

f.savefig('Figure_2.pdf',bbox_inches='tight')