# 🎓 Actividad Formativa 3 – Filtros Digitales en Python

👩‍💻 **Nombre:** Mayra  
📚 **Materia:** Programación de Señales  
📅 **Fecha:** Agosto 2026  

---

## ✨ Introducción
En esta actividad se implementaron **filtros digitales en Python** para analizar señales con ruido.  
El objetivo fue aplicar conceptos de procesamiento digital de señales, diseñando filtros Butterworth y observando su efecto sobre una señal compuesta de diferentes frecuencias.

---

## ⚙️ Simulación
El código (`Actividad 3.py`) genera una señal de prueba formada por:  
- Una componente de **50 Hz**  
- Una componente de **200 Hz**  
- Ruido aleatorio  

Posteriormente se diseñaron filtros digitales con la librería `scipy.signal` para atenuar las frecuencias no deseadas y mejorar la calidad de la señal.

---

## 📊 Resultados
La siguiente gráfica muestra la señal original con ruido y el resultado tras aplicar un filtro pasa bajos:

![Resultados del filtro](resultados_filtros.png)

Se observa que el filtro elimina gran parte de la componente de alta frecuencia y del ruido, conservando la señal de baja frecuencia.

---

## ✅ Conclusión
El uso de filtros digitales permite **separar componentes de frecuencia** y reducir el ruido en señales reales.  
Esta práctica refuerza la importancia de comprender parámetros como la frecuencia de corte y el orden del filtro para obtener resultados óptimos en aplicaciones de procesamiento de señales.

---

## 🛠️ Tecnologías utilizadas
- Python 3.x  
- Librerías: `numpy`, `matplotlib`, `scipy.signal`  
- Entorno: Visual Studio Code  

---

## 🚀 Cómo ejecutar
1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/Minyongi17/Actividad-Formativa-3-Filtros-Digitales.git

