"""
Classification Metrics: Confusion Matrix, Precision, Recall, and F1-Score
"""
import numpy as np

def compute_classification_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "TP": int(tp), "TN": int(tn), "FP": int(fp), "FN": int(fn),
        "Accuracy": round(accuracy, 4),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "F1-Score": round(f1, 4)
    }

if __name__ == "__main__":
    actual = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
    predicted = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
    metrics = compute_classification_metrics(actual, predicted)
    for k, v in metrics.items():
        print(f"{k:12}: {v}")
