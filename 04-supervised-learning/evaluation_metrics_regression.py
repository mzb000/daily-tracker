"""
Regression Evaluation Metrics Implementation
Formulas and implementations for MAE, MSE, RMSE, and R2-Score.
"""
import numpy as np

def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))

def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))

def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))

def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    return float(1 - (ss_residual / ss_total))

if __name__ == "__main__":
    actual = np.array([3.0, -0.5, 2.0, 7.0])
    predicted = np.array([2.5, 0.0, 2.0, 8.0])

    print("MAE :", mean_absolute_error(actual, predicted))
    print("MSE :", mean_squared_error(actual, predicted))
    print("RMSE:", root_mean_squared_error(actual, predicted))
    print("R2  :", r2_score(actual, predicted))
