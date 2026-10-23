"""
Vectorization Benchmark: Pure Python Loops vs NumPy Vectorized Operations
Understanding why vectorization is essential for Data Science and Deep Learning.
"""
import time
import numpy as np

def benchmark():
    size = 1_000_000
    py_list = list(range(size))
    np_arr = np.arange(size, dtype=np.float64)

    # Python loop
    t0 = time.perf_counter()
    py_result = [x * 2.5 for x in py_list]
    py_time = time.perf_counter() - t0

    # NumPy vectorized
    t0 = time.perf_counter()
    np_result = np_arr * 2.5
    np_time = time.perf_counter() - t0

    print(f"Python list loop time: {py_time:.4f}s")
    print(f"NumPy vectorized time: {np_time:.4f}s")
    print(f"NumPy speedup factor: {py_time / np_time:.1f}x faster!")

if __name__ == "__main__":
    benchmark()
