import numpy as np

# Generate random F1 scores for testing and validation datasets separately
random_f1_test = np.random.rand()  # Random F1 score for testing dataset
random_f1_val = np.random.rand()   # Random F1 score for validation dataset

# Display the randomly generated F1 scores
print(f"Random F1 Score for Testing Dataset: {random_f1_test:.4f}")
print(f"Random F1 Score for Validation Dataset: {random_f1_val:.4f}")
