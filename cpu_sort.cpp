#include "cpu_sort.h"
#include <omp.h>
#include <algorithm>

void cpu_sort(std::vector<int>& arr, int num_threads) {
    omp_set_num_threads(num_threads);
    #pragma omp parallel
    {
        #pragma omp single
        {
            std::sort(arr.begin(), arr.end());
        }
    }
}
