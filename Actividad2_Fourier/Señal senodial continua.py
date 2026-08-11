import numpy as np
import matplotlib.pyplot as plt

# Señal senoidal continua
x = np.arange(0, 1, 0.01)
y = np.sin(2 * np.pi * 5 * x)
plt.plot(x, y)
plt.title("Señal senoidal continua")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.savefig("imagenes/senoidal_continua.png")
plt.show()
plt.close()   # 👉 Esto limpia la figura

# Señal senoidal discreta
n = np.arange(0, 20)
x_discreta = np.sin(0.3 * np.pi * n)
plt.stem(n, x_discreta)
plt.title("Señal senoidal discreta")
plt.xlabel("n (muestras)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.savefig("imagenes/senoidal_discreta.png")
plt.show()
plt.close()

