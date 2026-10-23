# 🚀 NumPy Quick Reference Cheat Sheet

A concise table of the most frequently used NumPy functions in production Machine Learning workflows.

| Operation | NumPy Function | Description |
| :--- | :--- | :--- |
| **Creation** | `np.zeros(shape)` / `np.ones(shape)` | Initialize array of zeros / ones |
| **Sequence** | `np.arange(start, stop, step)` | Evenly spaced values within interval |
| **Linspace** | `np.linspace(start, stop, num)` | Evenly spaced numbers over a specified interval |
| **Reshape** | `arr.reshape(m, n)` | Rearrange dimensions without copying data |
| **Flatten** | `arr.ravel()` / `arr.flatten()` | Flatten multidimensional array to 1D |
| **Concatenate** | `np.hstack((a, b))` / `np.vstack((a, b))` | Stack arrays horizontally or vertically |
| **Dot Product** | `A @ B` or `np.matmul(A, B)` | Matrix multiplication |
| **Statistics** | `np.mean(a, axis=0)`, `np.std(a)` | Calculate mean and standard deviation |
| **Argmax** | `np.argmax(a, axis=1)` | Indices of maximum values (common in softmax output) |
| **Condition** | `np.where(condition, x, y)` | Vectorized if-else condition |
