"""
Handling Missing Data in Pandas
Strategies: Detection, Dropping, Mean/Median/Mode Imputation, and Forward/Backward Fill.
"""
import numpy as np
import pandas as pd

def handle_missing_values():
    df = pd.DataFrame({
        "age": [22, np.nan, 29, 35, np.nan, 28],
        "salary": [45000, 52000, np.nan, 68000, 70000, np.nan],
        "department": ["Sales", "IT", "HR", np.nan, "IT", "Sales"]
    })

    print("Missing count per column:\n", df.isnull().sum())

    # 1. Numerical Imputation using Median (robust to outliers)
    age_median = df["age"].median()
    df["age_imputed"] = df["age"].fillna(age_median)

    # 2. Categorical Imputation using Mode (most frequent)
    dept_mode = df["department"].mode()[0]
    df["department_imputed"] = df["department"].fillna(dept_mode)

    print("\nCleaned DataFrame:\n", df)

if __name__ == "__main__":
    handle_missing_values()
