"""
Random Sampling & Reproducibility in Data Science
Generating standard distributions (Normal, Uniform, Binomial) with fixed seeds.
"""
import numpy as np

def generate_distributions():
    # Setting seed guarantees reproducibility across team members and experiments
    rng = np.random.default_rng(seed=42)

    # Standard Normal distribution (Mean = 0, Std = 1)
    normal_data = rng.normal(loc=0.0, scale=1.0, size=1000)
    print(f"Normal Sample - Mean: {np.mean(normal_data):.3f}, Std: {np.std(normal_data):.3f}")

    # Uniform distribution between 10 and 50
    uniform_data = rng.uniform(low=10.0, high=50.0, size=1000)
    print(f"Uniform Sample - Min: {np.min(uniform_data):.2f}, Max: {np.max(uniform_data):.2f}")

    # Synthetic train/test split index shuffle
    indices = np.arange(100)
    rng.shuffle(indices)
    print("Shuffled indices sample (first 10):", indices[:10])

if __name__ == "__main__":
    generate_distributions()
