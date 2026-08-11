import numpy as np
import matplotlib.pyplot as plt

# Señal senoidal continua
t = np.linspace(0, 1, 500)
x = np.sin(2 * np.pi * 5 * t)

plt.plot(t, x)
plt.title("Señal senoidal continua")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Señal discreta
n = np.arange(0, 20)
x_discreta = np.sin(0.3 * np.pi * n)

plt.stem(n, x_discreta)
plt.title("Señal senoidal discreta")
plt.xlabel("n (muestras)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.savefig("imagenes/senoidal.png")
plt.show()
