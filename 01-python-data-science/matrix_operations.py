"""
Matrix Operations: Inverses, Determinants, and Eigenvalues
Practical implementation of core linear algebra using numpy.linalg.
"""
import numpy as np

def matrix_decomposition():
    A = np.array([[4, -2], [1,  1]], dtype=np.float64)

    # Determinant
    det_A = np.linalg.det(A)
    print("Determinant of A:", det_A)

    # Matrix Inverse (if det != 0)
    if det_A != 0:
        inv_A = np.linalg.inv(A)
        print("Inverse of A:\n", inv_A)
        # Verify identity: A @ A_inv = I
        print("Verification (A @ inv_A):\n", np.round(A @ inv_A, 2))

    # Eigenvalues and Eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)

if __name__ == "__main__":
    matrix_decomposition()
