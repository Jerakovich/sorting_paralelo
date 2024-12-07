#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;

// Función para inicializar el array con números aleatorios
void initialize_array(vector<int>& array) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(0, 1000000);
    for (auto& val : array)
        val = dist(gen);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Uso: ./prog <n>\n";
        return EXIT_FAILURE;
    }

    // Tamaño del array
    size_t n = stoull(argv[1]);

    // Crear e inicializar el array
    vector<int> array(n);
    initialize_array(array);

    // Ordenar usando std::sort y medir el tiempo
    auto start = chrono::high_resolution_clock::now();
    std::sort(array.begin(), array.end());
    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = end - start;

    cout << "Tiempo std::sort: " << elapsed.count() << " segundos\n";

    return 0;
}
