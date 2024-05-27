import numpy as np
import matplotlib.pyplot as plt
import time

# Measure time to generate 10,000 random numbers using np.random.rand()
n_samples = 10000
start_time = time.time()
random_numbers_np = np.random.rand(n_samples)
np_time = time.time() - start_time

# Print the result
print(f"np.random.rand() generation time: {np_time:.6f} seconds")