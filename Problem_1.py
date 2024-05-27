import numpy as np
import matplotlib.pyplot as plt

# Parameters for the LCG
a = 1664525
c = 1013904223
m = 2**32
seed = 123456789

def lcg(a, c, m, seed, size):
    numbers = []
    x = seed
    for _ in range(size):
        x = (a * x + c) % m
        numbers.append(x / m)  # Normalize to [0, 1)
    return numbers

# Generate 10,000 random numbers using the LCG
n_samples = 10000
random_numbers = lcg(a, c, m, seed, n_samples)

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
plt.title('Density Histogram of LCG Random Numbers vs. Uniform PDF')
plt.show()

f.savefig('Figure_1.pdf',bbox_inches='tight')