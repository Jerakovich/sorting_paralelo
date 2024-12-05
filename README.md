*Primero se debe instalar las dependencias* : 
- sudo apt-get update
- sudo apt install nvidia-cuda-toolkit


*Ejecucion:*

- Ejecutar como: ./prog <n> <modo> <nt>
- ./prog $((2**20)) 0 8 -> 0= modo CPU; 8-> numero de threads
- ./prog $((2**20)) 1 0 -> 1= modo GPU
