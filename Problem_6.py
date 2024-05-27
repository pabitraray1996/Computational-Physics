import numpy as np
import matplotlib.pyplot as plt

# Define the target distribution function f(x)
def target_distribution(x):
    return np.sqrt(2 / np.pi) * np.exp(-x**2 / 2)

# Rejection sampling function
def rejection_sampling(n_samples):
    samples = []
    c = np.sqrt(2 / np.pi)  # Normalizing constant

    while len(samples) < n_samples:
        x = np.random.uniform(0,20)  # Sample from the proposal distribution
        u = np.random.uniform(0, c)
        if u < target_distribution(x):
            samples.append(x)

    return np.array(samples)

# Generate 10,000 random numbers using rejection sampling
n_samples = 10000
random_numbers = rejection_sampling(n_samples)

f= plt.figure()
# Plot the density histogram
plt.hist(random_numbers, bins=100, density=True, alpha=0.6, color='g', label='Histogram')

# Plot the target distribution for comparison
x = np.linspace(0, max(random_numbers), 1000)
plt.plot(x, target_distribution(x), 'r-', lw=2, label='Target Distribution')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of Rejection Sampled Numbers vs. Target Distribution')
plt.legend()
plt.show()

f.savefig('Figure_6.pdf',bbox_inches='tight')