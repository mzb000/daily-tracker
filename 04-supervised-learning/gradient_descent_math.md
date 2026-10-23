# 🧠 Gradient Descent Intuition and Mathematics

Gradient descent is the optimization engine powering both simple linear regression and billion-parameter deep learning models.

---

## 1. The Cost Function (Mean Squared Error)
For $m$ training examples:
$$J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)^2$$
Where $\hat{y}^{(i)} = w x^{(i)} + b$.

The factor $\frac{1}{2}$ cancels out neatly when taking the derivative.

---

## 2. Gradient Calculation (Partial Derivatives)
Using the chain rule:
$$\frac{\partial J}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right) x^{(i)}$$
$$\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)$$

---

## 3. Parameter Update Rule
At each iteration:
$$w := w - \alpha \frac{\partial J}{\partial w}$$
$$b := b - \alpha \frac{\partial J}{\partial b}$$

Where $\alpha$ is the **Learning Rate**:
- **Too small $\alpha$**: Extremely slow convergence.
- **Too large $\alpha$**: Overshoots minimum, diverges.
