import numpy as np
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool, cpu_count

# Función ficticia para simular el benchmark
def sort_cpu(arr):
    return sorted(arr)

def sort_gpu(arr):
    time.sleep(0.001)  # Simular tiempo de GPU
    return sorted(arr)

def benchmark_sort_cpu(arr, num_threads=1):
    # Simulación de paralelismo con multiprocesos
    chunk_size = len(arr) // num_threads
    chunks = [arr[i * chunk_size: (i + 1) * chunk_size] for i in range(num_threads)]
    with Pool(num_threads) as p:
        sorted_chunks = p.map(sorted, chunks)
    return sorted([item for sublist in sorted_chunks for item in sublist])

# Benchmark para CPU y GPU
def run_benchmark():
    n_values = [10**i for i in range(3, 9)]  # Desde 1,000 hasta 100 millones
    cpu_times = []
    gpu_times = []

    for n in n_values:
        arr = np.random.randint(0, 1000, n).tolist()
        # Benchmark CPU
        start = time.time()
        sort_cpu(arr)
        cpu_times.append(time.time() - start)

        # Benchmark GPU
        start = time.time()
        sort_gpu(arr)
        gpu_times.append(time.time() - start)

    # Gráfico Tiempo vs n
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, cpu_times, label="CPU", marker='o')
    plt.plot(n_values, gpu_times, label="GPU", marker='o')
    plt.xscale('log')
    plt.xlabel('Tamaño del array (n)')
    plt.ylabel('Tiempo (s)')
    plt.title('Tiempo vs Tamaño del Array')
    plt.grid()
    plt.legend()
    plt.show()

    # CPU Speedup y Eficiencia
    num_threads = list(range(1, cpu_count() + 1))
    speedups_cpu = []
    efficiencies_cpu = []
    arr = np.random.randint(0, 1000, 10**6).tolist()

    for threads in num_threads:
        base_time = cpu_times[0]  # Tiempo con 1 hilo
        start = time.time()
        benchmark_sort_cpu(arr, num_threads=threads)
        elapsed_time = time.time() - start
        speedup = base_time / elapsed_time
        efficiency = speedup / threads
        speedups_cpu.append(speedup)
        efficiencies_cpu.append(efficiency)

    plt.figure(figsize=(10, 6))
    plt.plot(num_threads, speedups_cpu, label="Speedup CPU", marker='o')
    plt.xlabel('Número de hilos')
    plt.ylabel('Speedup')
    plt.title('Speedup CPU vs Número de Hilos')
    plt.grid()
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(num_threads, efficiencies_cpu, label="Eficiencia CPU", marker='o')
    plt.xlabel('Número de hilos')
    plt.ylabel('Eficiencia')
    plt.title('Eficiencia CPU vs Número de Hilos')
    plt.grid()
    plt.legend()
    plt.show()

    # GPU Speedup y Eficiencia
    num_blocks = [2**i for i in range(1, 6)]
    speedups_gpu = []
    efficiencies_gpu = []
    base_time = gpu_times[0]  # Tiempo con 1 bloque

    for blocks in num_blocks:
        start = time.time()
        sort_gpu(arr)  # Simulación con bloques
        elapsed_time = time.time() - start
        speedup = base_time / elapsed_time
        efficiency = speedup / blocks
        speedups_gpu.append(speedup)
        efficiencies_gpu.append(efficiency)

    plt.figure(figsize=(10, 6))
    plt.plot(num_blocks, speedups_gpu, label="Speedup GPU", marker='o')
    plt.xlabel('Número de bloques')
    plt.ylabel('Speedup')
    plt.title('Speedup GPU vs Número de Bloques')
    plt.grid()
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(num_blocks, efficiencies_gpu, label="Eficiencia GPU", marker='o')
    plt.xlabel('Número de bloques')
    plt.ylabel('Eficiencia')
    plt.title('Eficiencia GPU vs Número de Bloques')
    plt.grid()
    plt.legend()
    plt.show()

    # Comparación con std::sort
    std_sort_times = [time.time() - start for start in n_values]  # Simular tiempos
    speedup_vs_std = [st / ct for st, ct in zip(std_sort_times, cpu_times)]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, speedup_vs_std, label="Speedup vs std::sort", marker='o')
    plt.xscale('log')
    plt.xlabel('Tamaño del array (n)')
    plt.ylabel('Speedup')
    plt.title('Speedup vs std::sort')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_benchmark()
