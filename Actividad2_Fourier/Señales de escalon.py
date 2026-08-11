import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1024
t = np.linspace(-1, 1, N)

u = np.where(t >= 0, 1, 0)  # Escalón unitario
U = np.fft.fft(u)
freq = np.fft.fftfreq(N, d=(t[1]-t[0]))

plt.subplot(2,1,1)
plt.plot(t, u)
plt.title("Función escalón en el tiempo")

plt.subplot(2,1,2)
plt.plot(freq, np.abs(U))
plt.title("Espectro de frecuencia del escalón")
plt.savefig("imagenes/escalón.png")
plt.show()
