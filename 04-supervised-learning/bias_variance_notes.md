# ⚖️ The Bias-Variance Tradeoff

The core fundamental tension in supervised machine learning.

---

## 1. High Bias (Underfitting)
- **Symptom**: Model is overly simplistic and cannot capture the underlying pattern.
- **Error**: High training error AND high test error.
- **Fixes**:
  - Increase model complexity (e.g., polynomial features, deeper trees).
  - Add more relevant input features.
  - Decrease regularization ($\lambda$).

---

## 2. High Variance (Overfitting)
- **Symptom**: Model memorizes noise and training data peculiarities instead of general patterns.
- **Error**: Very low training error, but high test error (poor generalization).
- **Fixes**:
  - Collect more training data.
  - Simplify model or prune trees.
  - Increase regularization ($L_1$ or $L_2$).
  - Apply Cross-Validation (K-Fold).
  - Use Ensemble methods (e.g., Random Forests reduce variance through averaging).
