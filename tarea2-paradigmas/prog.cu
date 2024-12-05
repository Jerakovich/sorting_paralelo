#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <omp.h>
#include <cuda_runtime.h>
#include <thrust/sort.h>
#include <thrust/device_vector.h>
#include <random>

#define CUDA_CHECK(err) if (err != cudaSuccess) { \
    std::cerr << "CUDA error: " << cudaGetErrorString(err) << std::endl; \
    exit(EXIT_FAILURE); \
}

// Función para inicializar el array con números aleatorios usando std::mt19937
void initialize_array(std::vector<int>& array) {
    std::mt19937 gen(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, 1000000);
    for (auto& val : array)
        val = dist(gen);
}

// Merge Sort paralelo usando OpenMP
void merge(std::vector<int>& array, int left, int mid, int right) {
    std::vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right)
        temp[k++] = (array[i] <= array[j]) ? array[i++] : array[j++];

    while (i <= mid) temp[k++] = array[i++];
    while (j <= right) temp[k++] = array[j++];

    for (int l = left; l <= right; ++l)
        array[l] = temp[l - left];
}

void merge_sort_parallel(std::vector<int>& array, int left, int right, int depth) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;

    if (depth > 0) {
        #pragma omp parallel sections
        {
            #pragma omp section
            merge_sort_parallel(array, left, mid, depth - 1);
            #pragma omp section
            merge_sort_parallel(array, mid + 1, right, depth - 1);
        }
    } else {
        merge_sort_parallel(array, left, mid, 0);
        merge_sort_parallel(array, mid + 1, right, 0);
    }

    merge(array, left, mid, right);
}

void sort_cpu(std::vector<int>& array, int num_threads) {
    omp_set_num_threads(num_threads);
    merge_sort_parallel(array, 0, array.size() - 1, omp_get_max_active_levels());
}

// Ordenamiento en GPU usando Thrust
void sort_gpu(std::vector<int>& array) {
    thrust::device_vector<int> d_array(array.begin(), array.end());
    thrust::sort(d_array.begin(), d_array.end());
    thrust::copy(d_array.begin(), d_array.end(), array.begin());
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        std::cerr << "Uso: ./prog <n> <modo> <nt>\n";
        return EXIT_FAILURE;
    }

    size_t n = std::stoull(argv[1]); // Tamaño del array
    int modo = std::stoi(argv[2]);  // Modo: 0 = CPU, 1 = GPU
    int nt = std::stoi(argv[3]);    // Número de threads para CPU

    // Crear e inicializar el array
    std::vector<int> array(n);
    initialize_array(array);

    double start, end;

    if (modo == 0) { // CPU
        start = omp_get_wtime();
        sort_cpu(array, nt);
        end = omp_get_wtime();
    } else if (modo == 1) { // GPU
        start = omp_get_wtime();
        sort_gpu(array);
        end = omp_get_wtime();
    } else {
        std::cerr << "Modo no válido: 0 (CPU), 1 (GPU)\n";
        return EXIT_FAILURE;
    }

    std::cout << "Tiempo: " << (end - start) << " segundos\n";
    return 0;
}
