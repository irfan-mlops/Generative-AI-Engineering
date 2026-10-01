"""
Problem 1: Calculate Classification Accuracy
You are given two lists:
- y_true: the actual class labels
- y_pred: the predicted class labels from a machine learning model

1. Use a function.
2. Use parameters y_true and y_pred.
3. Compare both lists.
4. Count the correct predictions.
5. Return the accuracy percentage.
6. Do not hard-code the answer.
7. Do not use sklearn.
8. Do not use an external library.

"""

def calculate_accuracy(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("The length of y_true and y_pred must be the same.")

    if len(y_true) == 0:
        raise ValueError("Input lists cannot be empty.")

    correct_predictions = sum(
        1 for true, pred in zip(y_true, y_pred)
        if true == pred
    )

    return (correct_predictions / len(y_true)) * 100

