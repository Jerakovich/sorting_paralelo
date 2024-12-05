CUDA_PATH := /usr/local/cuda
CC := nvcc
CFLAGS := -O2 -Xcompiler -fopenmp
TARGET := prog

all: $(TARGET)

$(TARGET): prog.cu
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)
