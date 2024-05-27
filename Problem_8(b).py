import random

# Number of random points
N = 1000000

# Count points inside the 10-dimensional sphere
M = 0

for _ in range(N):
    point = [random.uniform(-1, 1) for _ in range(10)]
    if sum(x**2 for x in point) <= 1:
        M += 1

# Calculate the volume
volume_sphere = 1024 * M / N
print("Estimated volume of the 10-dimensional sphere:", volume_sphere)