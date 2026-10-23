"""
NumPy Basics: Array Creation, Shapes, and Data Types
Practical reference for high-performance numerical computing in Python.
"""
import numpy as np

def demonstrate_array_creation():
    # 1D Array (Vector)
    vec = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    print("Vector:", vec, "Shape:", vec.shape)

    # 2D Array (Matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
    print("Matrix:\n", matrix, "Shape:", matrix.shape)

    # Common initialization utilities
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    identity = np.eye(3)
    linear_space = np.linspace(0, 10, 5)  # 5 evenly spaced points between 0 and 10

    print("Identity matrix:\n", identity)
    print("Linspace array:", linear_space)

if __name__ == "__main__":
    demonstrate_array_creation()
