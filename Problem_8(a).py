import random

# Number of random points
N = 1000000

# Count points inside the circle
M = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        M += 1

# Calculate the area
area_circle = 4 * M / N
print("Estimated area of the circle:", area_circle)