import numpy as np
import matplotlib.pyplot as plt


# Define the sinc function
def f(x):
    if (x==0):
        return 1
    else:
        return np.sin(x)/x
    

# Define the analytical Fourier transform of sinc function
def analytical_fourier_transform(freq):
    return np.sqrt(np.pi/8) *(np.sign(1+freq)+np.sign(1-freq))


xmin = -50
xmax = 50
N = 200
delx = (xmax-xmin)/(N-1)
z=np.linspace(xmin,xmax,N)


sample =[]
for i in range(N):
    sample.append(f(xmin+i*delx))



dft = np.fft.fft(sample,norm='ortho')
k = (2*np.pi/delx)*np.fft.fftfreq(N)               #JUST GIVES q/N

sorted = []

for i in range(N):
    sorted.append([k[i],dft[i]])

sorted.sort(key=lambda x:x[0])

final_k,final_dft = [],[]
for l in range(N):
    final_dft.append(delx*(N/(2*np.pi))**0.5*np.exp(-1j*xmin*sorted[l][0])*sorted[l][1])
    final_k.append(sorted[l][0])


# Compute the analytical Fourier transform
final_anl=[]
for i in range(N):
    final_anl.append(analytical_fourier_transform(final_k[i]))



plt.subplot(2, 1, 1)
plt.plot(z,sample, label="sinc(x)")
plt.title("Sinc Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()




plt.subplot(2, 1, 2)
plt.plot(final_k,final_anl, label='Analytical')
plt.plot(final_k,final_dft, label='Numerical', linestyle='--')
plt.xlabel("$\omega$")
plt.ylabel("F($\omega$)")
plt.xlim(-5,5)
plt.grid()
plt.legend()
plt.show()