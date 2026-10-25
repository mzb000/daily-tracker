"""
Automated unit verification for EDA preprocessing functions.
"""
import numpy as np

def test_minmax_scaler():
    arr = np.array([0.0, 50.0, 100.0])
    scaled = (arr - arr.min()) / (arr.max() - arr.min())
    assert scaled[0] == 0.0
    assert scaled[-1] == 1.0
    print("✅ test_minmax_scaler passed")

def test_standard_scaler():
    arr = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    scaled = (arr - arr.mean()) / arr.std()
    assert abs(scaled.mean()) < 1e-7
    assert abs(scaled.std() - 1.0) < 1e-7
    print("✅ test_standard_scaler passed")

if __name__ == "__main__":
    test_minmax_scaler()
    test_standard_scaler()
    print("\n🎉 All Module 03 verification tests passed cleanly!")
