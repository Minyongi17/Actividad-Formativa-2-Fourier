import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1024
t = np.linspace(0, 1, N)

# Pulso rectangular: valor 1 en el centro, 0 fuera
x = np.where(np.abs(t - 0.5) < 0.25, 1, 0)

# Transformada de Fourier
X = np.fft.fft(x)
freq = np.fft.fftfreq(N, d=t[1] - t[0])

# Gráficas
plt.subplot(2,1,1)
plt.plot(t, x)
plt.title("Pulso rectangular")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.plot(freq, np.abs(X))
plt.title("Espectro de magnitud del pulso")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")

# 👉 Guardar la gráfica en la carpeta imagenes
plt.savefig("imagenes/pulso.png")
plt.show()
plt.close()
