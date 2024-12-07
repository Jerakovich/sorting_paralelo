import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatter

# Todos estos datos fueron sacados del script prog.cu
n_values = [2**20, 2**22, 2**24, 2**26, 2**28]  # Tamaños del array
cpu_times_1_thread = [0.39254, 1.5886, 6.50969, 26.6334, 106.516]  # Tiempos con 1 hilo ===> ./prog $((2**x)) 0 1
cpu_times_4_threads = [0.491174,0.958282,3.83568,15.9351, 67.8596]  # Tiempos con 4 hilos ===> ./prog $((2**x)) 0 4
cpu_times_8_threads = [0.235169, 0.966208, 3.93584, 15.7743, 73.9135]  # Tiempos con 8 hilos ===> ./prog $((2**x)) 0 8
gpu_times = [1.29582,1.32975, 1.3563, 1.52851, 5.02381]  # Tiempos en GPU ===> ./prog $((2**x)) 1 0
std_sort_times = [0.373016,1.73381,7.11328,29.9326,128.909]  # Tiempos de std::sort

# Gráfico 1: Tiempo vs Tamaño del Array del cpu y gpu
plt.figure(figsize=(10, 6))
plt.plot(n_values, cpu_times_1_thread, label="CPU (1 hilo)", marker='o')
plt.plot(n_values, cpu_times_4_threads, label="CPU (4 hilos)", marker='o')
plt.plot(n_values, cpu_times_8_threads, label="CPU (8 hilos)", marker='o')
plt.plot(n_values, gpu_times, label="GPU", marker='o')

plt.xscale('log')
plt.yscale('linear')
plt.xlabel('Tamaño del array (n)')
plt.ylabel('Tiempo (segundos)')
plt.title('Tiempo de Ejecución vs. Tamaño del Arreglo')
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.show()

# Gráfico 2: Speedup (CPU y GPU) vs Tamaño del Array
speedup_cpu_8_threads = np.array(std_sort_times) / np.array(cpu_times_8_threads)
speedup_cpu_4_threads = np.array(std_sort_times) / np.array(cpu_times_4_threads)    # CPU 1 hilo vs 4 hilos
speedup_gpu = np.array(std_sort_times) / np.array(gpu_times)  # GPU vs CPU (1 hilo)

plt.figure(figsize=(10, 6))
plt.plot(n_values, speedup_cpu_8_threads, label="Speedup (CPU, 8 hilos)", marker='o')
plt.plot(n_values, speedup_gpu, label="Speedup (GPU)", marker='o')

plt.xscale('log')
plt.xlabel('Tamaño del array (n)')
plt.ylabel('Speedup')
plt.title('Speedup vs. Tamaño del Arreglo')
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.show()

# Gráfico 3: Eficiencia Paralela (CPU) vs Número de hilos
threads = [1, 4, 8]  # hilos usados
speedup_per_thread = [1, speedup_cpu_4_threads[-1], speedup_cpu_8_threads[-1]]  # Usar speedup de 1 hilo y 8 hilos
efficiency_cpu = np.array(speedup_per_thread) / np.array(threads)  # Eficiencia = Speedup / Hilos

plt.figure(figsize=(10, 6))
plt.plot(threads, efficiency_cpu, marker='o', label='Eficiencia paralela (CPU)')
plt.xlabel('Número de hilos')
plt.ylabel('Eficiencia paralela')
plt.title('Eficiencia Paralela vs. Número de Hilos (CPU)')
plt.grid()
plt.legend()
plt.show()

# Gráfico 4: Speedup (GPU) vs Número de Bloques
blocks = [1, 8]  # Número de bloques utilizados
gpu_times_1_block = [2.11553]  # Tiempo con 1 bloque
gpu_times_8_blocks = [1.52851]  # Tiempo con 8 bloques

# Calcular speedup 
speedup_gpu_blocks = [gpu_times_1_block[0] / gpu_times_1_block[0], 
                      gpu_times_1_block[0] / gpu_times_8_blocks[0]] 

plt.figure(figsize=(10, 6))
plt.plot(blocks, speedup_gpu_blocks, marker='o', label='Speedup (GPU)')
plt.xlabel('Número de bloques')
plt.ylabel('Speedup')
plt.title('Speedup vs. Número de Bloques (GPU)')
plt.grid()
plt.legend()
plt.show()

# Gráfico 5: Eficiencia Paralela (GPU) vs Número de Bloques
efficiency_gpu = np.array(speedup_gpu_blocks) / np.array(blocks)

plt.figure(figsize=(10, 6))
plt.plot(blocks, efficiency_gpu, marker='o', label='Eficiencia paralela (GPU)')
plt.xlabel('Número de bloques')
plt.ylabel('Eficiencia paralela')
plt.title('Eficiencia Paralela vs. Número de Bloques (GPU)')
plt.grid()
plt.legend()
plt.show()

# Gráfico 6 
plt.figure(figsize=(10, 6))

plt.plot(n_values, speedup_cpu_4_threads, marker='o', label='Speedup CPU (4 hilos)')
plt.plot(n_values, speedup_cpu_8_threads, marker='o', label='Speedup CPU (8 hilos)')
plt.plot(n_values, speedup_gpu, marker='o', label='Speedup GPU')

plt.xscale('log')
plt.yscale('linear')

plt.xlabel('Tamaño del array (n)', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Speedup vs Tamaño del array (n)', fontsize=14)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()
