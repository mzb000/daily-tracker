# 📐 Linear Algebra Fundamentals for Machine Learning

Understanding linear algebra is crucial for intuition in regression, neural networks, and PCA.

---

## 1. Dot Product (Inner Product)
For vectors $\mathbf{u}$ and $\mathbf{v}$ of length $n$:
$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)$$

- **Geometric meaning**: Measures directional alignment and projection of one vector onto another.
- **In Neural Networks**: Layer activations compute $\mathbf{z} = \mathbf{W} \mathbf{x} + \mathbf{b}$ via dot products.

---

## 2. Matrix Multiplication Compatibility
Two matrices $A$ ($m \times k$) and $B$ ($k \times p$) can be multiplied because the inner dimension $k$ matches.
Result matrix $C = AB$ has dimension $m \times p$.

```python
import numpy as np

A = np.random.randn(3, 4)
B = np.random.randn(4, 2)
C = np.matmul(A, B)  # or A @ B -> Shape (3, 2)
```

---

## 3. Vector Norms (L1 vs L2)
- **L1 Norm (Manhattan)**: $\|\mathbf{x}\|_1 = \sum |x_i|$ (Encourages sparsity, used in Lasso regression)
- **L2 Norm (Euclidean)**: $\|\mathbf{x}\|_2 = \sqrt{\sum x_i^2}$ (Penalizes large weights, used in Ridge regression)
