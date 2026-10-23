"""
Regularization: Ridge (L2) and Lasso (L1) Regression
Prevents overfitting by penalizing large model weights.
"""
import numpy as np

def ridge_loss(y_true, y_pred, weights, lambda_param: float = 0.1):
    # L2 penalty: lambda * sum(w^2)
    mse = np.mean((y_true - y_pred) ** 2)
    l2_penalty = lambda_param * np.sum(weights ** 2)
    return mse + l2_penalty

def lasso_loss(y_true, y_pred, weights, lambda_param: float = 0.1):
    # L1 penalty: lambda * sum(|w|) -> encourages sparse weights
    mse = np.mean((y_true - y_pred) ** 2)
    l1_penalty = lambda_param * np.sum(np.abs(weights))
    return mse + l1_penalty

if __name__ == "__main__":
    weights = np.array([4.2, -0.05, 3.1, -5.8])
    y_true = np.array([10.0, 15.0])
    y_pred = np.array([9.5, 14.8])

    r_loss = ridge_loss(y_true, y_pred, weights, lambda_param=0.5)
    l_loss = lasso_loss(y_true, y_pred, weights, lambda_param=0.5)

    print(f"Ridge Loss (L2): {r_loss:.4f}")
    print(f"Lasso Loss (L1): {l_loss:.4f}")
