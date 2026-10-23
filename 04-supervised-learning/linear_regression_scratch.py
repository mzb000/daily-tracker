"""
Linear Regression from Scratch using Pure NumPy
Implements the Hypothesis function, MSE Cost function, and Batch Gradient Descent.
"""
import numpy as np

class LinearRegressionScratch:
    def __init__(self, learning_rate: float = 0.01, iterations: int = 1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = 0.0
        self.cost_history = []

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for _ in range(self.iterations):
            # 1. Forward Pass (Hypothesis)
            y_pred = np.dot(X, self.weights) + self.bias

            # 2. Compute Mean Squared Error (MSE)
            error = y_pred - y
            cost = (1 / (2 * n_samples)) * np.sum(error ** 2)
            self.cost_history.append(cost)

            # 3. Compute Gradients
            dw = (1 / n_samples) * np.dot(X.T, error)
            db = (1 / n_samples) * np.sum(error)

            # 4. Update Parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.dot(X, self.weights) + self.bias

if __name__ == "__main__":
    # Test on synthetic data: y = 3x + 4 + noise
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 3 * X.squeeze() + 4 + np.random.randn(100) * 0.1

    model = LinearRegressionScratch(learning_rate=0.1, iterations=500)
    model.fit(X, y)
    print(f"Trained Weight (True ~ 3.0): {model.weights[0]:.3f}")
    print(f"Trained Bias   (True ~ 4.0): {model.bias:.3f}")
