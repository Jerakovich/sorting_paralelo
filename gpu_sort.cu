#include "gpu_sort.cuh"
#include <thrust/sort.h>
#include <thrust/device_vector.h>

void gpu_sort(std::vector<int>& arr) {
    thrust::device_vector<int> d_arr(arr.begin(), arr.end());
    thrust::sort(d_arr.begin(), d_arr.end());
    thrust::copy(d_arr.begin(), d_arr.end(), arr.begin());
}
