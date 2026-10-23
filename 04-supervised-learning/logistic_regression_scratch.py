"""
Logistic Regression from Scratch
Classification algorithm using Sigmoid activation and Binary Cross-Entropy Loss.
"""
import numpy as np

def sigmoid(z: np.ndarray) -> np.ndarray:
    # Stable sigmoid with clipping to prevent overflow
    z_clipped = np.clip(z, -500, 500)
    return 1.0 / (1.0 + np.exp(-z_clipped))

class LogisticRegressionScratch:
    def __init__(self, lr: float = 0.05, iterations: int = 1000):
        self.lr = lr
        self.iterations = iterations
        self.weights = None
        self.bias = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for _ in range(self.iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = sigmoid(linear_model)

            # Gradient calculation
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return sigmoid(np.dot(X, self.weights) + self.bias)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        return (self.predict_proba(X) >= threshold).astype(int)

if __name__ == "__main__":
    X = np.array([[1.0, 2.0], [2.0, 3.0], [5.0, 6.0], [6.0, 7.0]])
    y = np.array([0, 0, 1, 1])

    clf = LogisticRegressionScratch(lr=0.1, iterations=1000)
    clf.fit(X, y)
    preds = clf.predict(X)
    print("Predictions (Expected [0, 0, 1, 1]):", preds)
