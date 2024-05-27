import numpy as np
import matplotlib.pyplot as plt

def target_density(x):
    "Target density function (uniform between 3 and 7)."
    if 3 < x < 7:
        return 1 / 4
    else:
        return 0

def metropolis_sampler(num_samples, initial_value, proposal_std):
    "Metropolis algorithm to sample from the target density."
    samples = np.zeros(num_samples)
    samples[0] = initial_value
    
    for i in range(1, num_samples):
        current_value = samples[i - 1]
        proposed_value = np.random.normal(current_value, proposal_std)
        
        # Calculate acceptance probability
        acceptance_ratio = target_density(proposed_value) / target_density(current_value)
        acceptance_ratio = min(1, acceptance_ratio)
        
        # Accept or reject the proposed value
        if np.random.rand() < acceptance_ratio:
            samples[i] = proposed_value
        else:
            samples[i] = current_value
    
    return samples

# Parameters
num_samples = 10000
initial_value = 5.0
proposal_std = 0.5

# Generate samples using the Metropolis algorithm
samples = metropolis_sampler(num_samples, initial_value, proposal_std)

# Plot the Markov Chain
f1=plt.figure(figsize=(12, 5))
plt.plot(samples, alpha=0.6)
plt.title('Markov Chain of Samples')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.grid(True)
plt.show()

f1.savefig('Figure_9(a).pdf',bbox_inches='tight')

# Plot the density histogram of the samples
f2=plt.figure(figsize=(12, 5))
plt.hist(samples, bins=50, density=True, alpha=0.7, label='Sampled Density')
plt.axhline(y=1/4, color='r', linestyle='--', label='True Density (Uniform)')
plt.xlim(2, 8)
plt.title('Density Histogram of Samples')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

f2.savefig('Figure_9(b).pdf',bbox_inches='tight')