"""
Outlier Detection and Remediation in Python
Comparing Trimming (dropping) vs Winsorizing (capping at percentiles).
"""
import numpy as np
import pandas as pd

def handle_outliers():
    np.random.seed(42)
    # Generate distribution with artificial extreme outliers
    data = np.concatenate([np.random.normal(50, 5, 100), [120, 135, -10]])
    df = pd.DataFrame({"metric": data})

    q1 = df["metric"].quantile(0.25)
    q3 = df["metric"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print(f"IQR Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")

    # Winsorizing / Capping (Best practice: clip to bounds without losing rows)
    df["metric_capped"] = df["metric"].clip(lower=lower_bound, upper=upper_bound)

    print("Original Max:", df["metric"].max())
    print("Capped Max:", df["metric_capped"].max())

if __name__ == "__main__":
    handle_outliers()
