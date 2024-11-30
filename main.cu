#include <iostream>
#include <vector>
#include <cstdlib>
#include <omp.h>
#include "cpu_sort.h"
#include "gpu_sort.cuh"

void generate_random_array(std::vector<int>& arr) {
    for (auto& num : arr) {
        num = rand() % 1000000;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        std::cerr << "Usage: ./prog <n> <mode> <num_threads>\n";
        return 1;
    }

    int n = std::atoi(argv[1]);
    int mode = std::atoi(argv[2]);
    int num_threads = std::atoi(argv[3]);

    std::vector<int> arr(n);
    generate_random_array(arr);

    double start_time, end_time;

    if (mode == 0) {
        // CPU Mode
        start_time = omp_get_wtime();
        cpu_sort(arr, num_threads);
        end_time = omp_get_wtime();
    } else if (mode == 1) {
        // GPU Mode
        start_time = omp_get_wtime();
        gpu_sort(arr);
        end_time = omp_get_wtime();
    } else {
        std::cerr << "Invalid mode! Use 0 for CPU and 1 for GPU.\n";
        return 1;
    }

    std::cout << "Time taken: " << (end_time - start_time) << " seconds\n";
    return 0;
}
