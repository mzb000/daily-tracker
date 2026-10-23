"""
GroupBy & Multi-level Aggregations
Summarizing grouped metrics efficiently across categories.
"""
import pandas as pd

def groupby_recipes():
    df = pd.DataFrame({
        "category": ["Electronics", "Electronics", "Clothing", "Clothing", "Home", "Home"],
        "region": ["North", "South", "North", "South", "North", "South"],
        "sales": [1200, 1500, 450, 700, 300, 850],
        "units": [4, 5, 9, 14, 2, 6]
    })

    # Multiple aggregations per column
    summary = df.groupby("category").agg({
        "sales": ["sum", "mean", "max"],
        "units": ["sum"]
    })
    print("Grouped Summary:\n", summary)

    # Pivot Table
    pivot = pd.pivot_table(df, values="sales", index="category", columns="region", aggfunc="sum", fill_value=0)
    print("\nPivot Table:\n", pivot)

if __name__ == "__main__":
    groupby_recipes()
