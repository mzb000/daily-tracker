"""
Ensemble Variance Reduction Verification
"""
import numpy as np

def simulate_ensemble_accuracy():
    # 10 independent classifiers, each with 70% accuracy
    np.random.seed(42)
    n_trials = 1000
    n_classifiers = 15
    p_correct = 0.70

    # Simulate predictions (1 = correct, 0 = wrong)
    preds = np.random.binomial(n=1, p=p_correct, size=(n_trials, n_classifiers))
    
    # Majority vote: ensemble is right if > 50% of classifiers are right
    majority_correct = np.mean(preds, axis=1) > 0.5
    ensemble_acc = np.mean(majority_correct)

    print(f"Individual Model Accuracy : {p_correct * 100:.1f}%")
    print(f"Ensemble Majority Accuracy: {ensemble_acc * 100:.1f}% (Boosted by collective voting!)")

if __name__ == "__main__":
    simulate_ensemble_accuracy()
