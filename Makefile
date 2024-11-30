CC = nvcc
CFLAGS = -Xcompiler -fopenmp

all: prog

prog: main.cu cpu_sort.cpp gpu_sort.cu
	$(CC) $(CFLAGS) -o prog main.cu cpu_sort.cpp gpu_sort.cu

clean:
	rm -f prog
