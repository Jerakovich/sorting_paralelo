import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatter

# Datos experimentales
n_values = [2**20, 2**22, 2**24, 2**26, 2**28]  # Tamaños del array
cpu_times_1_thread = [0.39254, 1.5886, 6.50969, 26.6334, 106.516]  # Tiempos con 1 hilo
cpu_times_8_threads = [0.235169, 0.966208, 3.93584, 15.7743, 73.9135]  # Tiempos con 8 hilos
gpu_times = [1.32975, 1.29582, 1.3563, 1.52851, 2.11553]  # Tiempos en GPU

# Gráfico 1: Tiempo vs Tamaño del Array
plt.figure(figsize=(10, 6))
plt.plot(n_values, cpu_times_1_thread, label="CPU (1 hilo)", marker='o')
plt.plot(n_values, cpu_times_8_threads, label="CPU (8 hilos)", marker='o')
plt.plot(n_values, gpu_times, label="GPU", marker='o')

# Usar escala logarítmica en el eje X para ver el tamaño del array en escala log
plt.xscale('log')
# Usar escala lineal en el eje Y para ver los tiempos de manera más natural
plt.yscale('linear')

plt.xlabel('Tamaño del array (n)')
plt.ylabel('Tiempo (segundos)')
plt.title('Tiempo de Ejecución vs. Tamaño del Array')

# Añadir grid
plt.grid(True, which="both", linestyle='--')

plt.legend()
plt.show()

# Speedup (CPU)
speedup_cpu = np.array(cpu_times_1_thread) / np.array(cpu_times_8_threads)


'''
# Gráfico 2: Speedup vs Número de Hilos (CPU)
threads = [1, 2, 4, 8]
speedup_values = speedup_cpu[:len(threads)]  # Selecciona valores correspondientes
plt.figure(figsize=(10, 6))
plt.plot(threads, speedup_values, marker='o', label='Speedup (CPU)')
plt.xlabel('Número de hilos')
plt.ylabel('Speedup')
plt.title('Speedup vs. Número de Hilos (CPU)')
plt.grid()
plt.legend()
plt.show()

# Eficiencia paralela
efficiency_values = speedup_values / np.array(threads)
plt.figure(figsize=(10, 6))
plt.plot(threads, efficiency_values, marker='o', label='Eficiencia paralela (CPU)')
plt.xlabel('Número de hilos')
plt.ylabel('Eficiencia paralela')
plt.title('Eficiencia paralela vs. Número de Hilos (CPU)')
plt.grid()
plt.legend()
plt.show()
'''