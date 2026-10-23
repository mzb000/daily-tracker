"""
NumPy Broadcasting and Advanced Indexing
Demonstrates how NumPy handles operations on arrays of different dimensions.
"""
import numpy as np

def demonstrate_broadcasting():
    # Broadcasting allows element-wise operations on arrays of different shapes
    matrix = np.array([[10, 20, 30], [40, 50, 60]])  # Shape (2, 3)
    bias = np.array([1, 2, 3])                        # Shape (3,) -> broadcasts to (2, 3)

    result = matrix + bias
    print("Original Matrix:\n", matrix)
    print("Added Bias (Broadcasting):\n", result)

def boolean_masking():
    data = np.array([12, 45, 67, 89, 23, 5, 91, 34])
    # Filter elements greater than 50
    mask = data > 50
    filtered = data[mask]
    print("Filtered (> 50):", filtered)

if __name__ == "__main__":
    demonstrate_broadcasting()
    boolean_masking()
