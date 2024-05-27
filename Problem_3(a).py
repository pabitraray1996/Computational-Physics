import numpy as np
import matplotlib.pyplot as plt
import time

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

# Measure time to generate 10,000 random numbers using the LCG
n_samples = 10000
start_time = time.time()
random_numbers_lcg = lcg(a, c, m, seed, n_samples)
lcg_time = time.time() - start_time

# Print the result
print(f"LCG generation time: {lcg_time:.6f} seconds")