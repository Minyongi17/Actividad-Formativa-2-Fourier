import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1024
t = np.linspace(-1, 1, N)
x = np.where(np.abs(t) < 0.5, 1, 0)  # Pulso rectangular

# Transformada de Fourier
X = np.fft.fft(x)
freq = np.fft.fftfreq(N, d=(t[1]-t[0]))

# Gráficas
plt.subplot(2,1,1)
plt.plot(t, x)
plt.title("Pulso rectangular en el tiempo")

plt.subplot(2,1,2)
plt.plot(freq, np.abs(X))
plt.title("Espectro de frecuencia (magnitud)")
plt.savefig("imagenes/pulso rectangular.png")
plt.show()