import numpy as np
import matplotlib.pyplot as plt

def box_muller_transform(u1, u2):
    z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    z1 = np.sqrt(-2.0 * np.log(u1)) * np.sin(2.0 * np.pi * u2)
    return z0, z1

# Generate 10,000 random numbers using the Box-Muller transform
n_samples = 10000
u1 = np.random.rand(n_samples // 2)
u2 = np.random.rand(n_samples // 2)

z0, z1 = box_muller_transform(u1, u2)

# Combine the two sets of generated numbers
gaussian_numbers = np.concatenate((z0, z1))

f= plt.figure()
# Plot the density histogram
plt.hist(gaussian_numbers, bins=100, density=True, alpha=0.6, color='g', label='Histogram')

# Plot the Gaussian PDF for comparison
x = np.linspace(-4, 4, 1000)
gaussian_pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
plt.plot(x, gaussian_pdf, 'r-', lw=2, label='Gaussian PDF')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Box-Muller Generated Numbers vs. Gaussian PDF')
plt.legend()
plt.show()

f.savefig('Figure_5.pdf',bbox_inches='tight')