"""
Self-verification test suite for Module 01 (NumPy Basics).
Ensures all code snippets execute with valid assertions.
"""
import numpy as np

def test_array_creation():
    arr = np.arange(10)
    assert arr.shape == (10,)
    assert arr.sum() == 45
    print("✅ test_array_creation passed")

def test_matrix_multiplication():
    A = np.eye(3)
    B = np.ones((3, 3))
    result = A @ B
    np.testing.assert_array_equal(result, B)
    print("✅ test_matrix_multiplication passed")

def test_broadcasting():
    a = np.array([1, 2, 3])
    b = 2
    np.testing.assert_array_equal(a * b, np.array([2, 4, 6]))
    print("✅ test_broadcasting passed")

if __name__ == "__main__":
    test_array_creation()
    test_matrix_multiplication()
    test_broadcasting()
    print("\n🎉 All Module 01 NumPy tests passed cleanly!")
