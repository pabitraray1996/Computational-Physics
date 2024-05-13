import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the .dat file
data = np.loadtxt('fftgsl.txt')

# Step 2: Plot the data
# Assuming your data has two columns (x, y), adjust this according to your data
x = np.fft.fftshift(data[:, 0])  # assuming x values are in the first column
y = np.fft.fftshift(data[:, 1])  # assuming y values are in the second column

plt.plot(x,y)
plt.xlabel("k")
plt.ylabel("F(k)")
plt.title("$sinc$ Fourier transform")
plt.grid(True)  # Add grid
plt.show()
