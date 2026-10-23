"""
Pandas DataFrames and Series: Creation and Core Properties
Essential structures for tabular data manipulation.
"""
import pandas as pd

def demonstrate_dataframe_basics():
    data = {
        "student_id": [101, 102, 103, 104, 105],
        "name": ["Aaliyah", "Bilal", "Chaudhry", "Danyal", "Emaan"],
        "score": [88.5, 92.0, 79.5, 85.0, 95.5],
        "passed": [True, True, True, True, True],
        "department": ["CS", "AI", "SE", "CS", "AI"]
    }

    df = pd.DataFrame(data)
    print("DataFrame Head:\n", df.head(3))
    print("\nData Types:\n", df.dtypes)
    print("\nSummary Statistics:\n", df.describe())

if __name__ == "__main__":
    demonstrate_dataframe_basics()
