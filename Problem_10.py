import numpy as np
import matplotlib.pyplot as plt
from math import *


meshlim = 100
meshsize = 3001
x = np.linspace(-meshlim, meshlim, meshsize)
y = np.linspace(-meshlim, meshlim, meshsize)
# full coordinate arrays
xx, yy = np.meshgrid(x, y)
zz = np.exp(-(xx**2 + yy**2))
xx.shape, yy.shape, zz.shape

Delta = 2*meshlim/(meshsize-1)
kx = (2*np.pi/(meshsize*Delta))*np.arange(-(meshsize-1)/2,(meshsize-1)/2+1)
ky = (2*np.pi/(meshsize*Delta))*np.arange(-(meshsize-1)/2,(meshsize-1)/2+1)
kxx, kyy = np.meshgrid(kx, ky)
kzz = 0.5*np.exp(-(kxx**2+kyy**2)/4)


omega = np.fft.fft2(zz,norm="ortho")
omega = np.fft.fftshift(omega)


factor = (Delta**2)*(meshsize/(2*np.pi))*np.exp(-1j*(kxx*np.min(x)+kyy*np.min(y)))
ft_omega = factor*omega


fig1 = plt.figure(figsize=(5,5))
ax1 = plt.axes(projection='3d')
ax1.contour3D(kxx, kyy, ft_omega,200)
ax1.view_init(15, 35)

fig2 = plt.figure(figsize=(5,5))
ax2 = plt.axes(projection='3d')
ax2.contour3D(kx, ky, kzz, 200)
ax2.view_init(15, 35)


plt.show()