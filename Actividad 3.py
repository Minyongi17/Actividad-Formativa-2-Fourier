import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# Señal de prueba: mezcla de 50 Hz y 200 Hz con ruido
fs = 1000  # frecuencia de muestreo
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*200*t)
signal_noisy = signal + 0.5*np.random.randn(len(t))

# Función para diseñar filtro Butterworth
def butter_filter(cutoff, fs, order=5, btype='low'):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return b, a

def apply_filter(data, cutoff, fs, order=5, btype='low'):
    b, a = butter_filter(cutoff, fs, order, btype)
    y = lfilter(b, a, data)
    return y

# Filtro pasa bajos (corte 100 Hz)
low_filtered = apply_filter(signal_noisy, 100, fs, order=6, btype='low')

# Filtro pasa altos (corte 100 Hz)
high_filtered = apply_filter(signal_noisy, 100, fs, order=6, btype='high')

# Filtro pasa bandas (50–150 Hz)
b, a = butter(6, [50/(0.5*fs), 150/(0.5*fs)], btype='band')
band_filtered = lfilter(b, a, signal_noisy)

# Graficar resultados
plt.figure(figsize=(12,8))
plt.subplot(4,1,1)
plt.plot(t, signal_noisy)
plt.title("Señal original con ruido")

plt.subplot(4,1,2)
plt.plot(t, low_filtered)
plt.title("Filtro pasa bajos (≤100 Hz)")

plt.subplot(4,1,3)
plt.plot(t, high_filtered)
plt.title("Filtro pasa altos (≥100 Hz)")

plt.subplot(4,1,4)
plt.plot(t, band_filtered)
plt.title("Filtro pasa bandas (50–150 Hz)")

plt.tight_layout()
plt.savefig("resultados_filtros.png")  # guarda las gráficas en un archivo PNG
plt.show()  # opcional, si quieres verlas en pantalla también
