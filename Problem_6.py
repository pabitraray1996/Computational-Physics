import numpy as np
import matplotlib.pyplot as plt

# Define the constant function
def constant_function(x, c):
    return np.ones_like(x) * c

# Define the Fourier transform
def fourier_transform(x, f_x):
    return np.fft.fftshift(np.fft.fft(f_x))

# Define the frequency array
def frequency_array(x):
    dx = x[1] - x[0]
    N = len(x)
    freq = np.fft.fftfreq(N, dx)
    return np.fft.fftshift(freq)

# Define the x range
x = np.linspace(-10, 10, 1000)

# Define the constant value
c = 5.0

# Compute the constant function
f_x = constant_function(x, c)

# Compute the Fourier transform
F_k = fourier_transform(x, f_x)

# Get the frequency array
freq = frequency_array(x)

# Plot the constant function
plt.subplot(2, 1, 1)
plt.plot(x, f_x)
plt.title('Constant Function: f(x) = {}'.format(c))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plot the Fourier transform
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(F_k))
plt.title('Fourier Transform')
plt.xlabel('Frequency (k)')
plt.ylabel('|F(k)|')
plt.grid()
plt.xlim(-5, 5)
plt.ylim(0, max(np.abs(F_k)) + 1)

plt.tight_layout()
plt.show()