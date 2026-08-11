import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1024                # número de muestras
t = np.linspace(0, 1, N) # vector de tiempo de 0 a 1 segundo
f0 = 5                  # frecuencia de la señal senoidal

# Señal senoidal
x_sin = np.sin(2*np.pi*f0*t)

# Transformada de Fourier
X_sin = np.fft.fft(x_sin)
freq = np.fft.fftfreq(N, d=(t[1]-t[0]))

# Gráficas
plt.subplot(2,1,1)
plt.plot(t, x_sin)
plt.title("Señal senoidal en el tiempo")

plt.subplot(2,1,2)
plt.plot(freq, np.abs(X_sin))
plt.title("Espectro de frecuencia de la senoidal")
plt.savefig("imagenes/senoidal con el tiempo.png")
plt.show()