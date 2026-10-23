"""
Combining Datasets: Merge, Join, and Concatenate
Essential recipes for feature joining and dataset assembly.
"""
import pandas as pd

def demonstrate_joins():
    users = pd.DataFrame({
        "user_id": [1, 2, 3, 4],
        "name": ["Zara", "Ahmed", "Fatima", "Hamza"]
    })

    transactions = pd.DataFrame({
        "tx_id": [101, 102, 103, 104],
        "user_id": [1, 2, 2, 5],
        "amount": [250.0, 120.5, 450.0, 90.0]
    })

    # Left Merge: Keep all users, attach transactions where present
    left_merged = pd.merge(users, transactions, on="user_id", how="left")
    print("Left Merge (Users with Transactions):\n", left_merged)

    # Inner Merge: Only users with existing transactions
    inner_merged = pd.merge(users, transactions, on="user_id", how="inner")
    print("\nInner Merge:\n", inner_merged)

if __name__ == "__main__":
    demonstrate_joins()
