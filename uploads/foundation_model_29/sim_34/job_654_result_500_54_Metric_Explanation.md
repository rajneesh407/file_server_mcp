
    ##### Accuracy
    Measures the overall correctness of predictions. It is the proportion of all instances (both positive and negative) that were correctly classified.
    **Formula:** `(Number of correct predictions) / (Total number of predictions)`

    ##### Precision
    Measures how many of the instances predicted as positive are actually positive. It reflects the quality of the positive predictions.
    **Formula:** `(True Positives) / (True Positives + False Positives)`

    ##### Recall (also called Sensitivity)
    Measures how many of the actual positive instances were correctly identified. It reflects the ability to find all positive cases.
    **Formula:** `(True Positives) / (True Positives + False Negatives)`

    ##### F1 Score
    The harmonic mean of precision and recall, providing a single metric that balances both. It is useful when you want a balance between precision and recall.
    **Formula:** `2 * (Precision * Recall) / (Precision + Recall)`

    ##### Kendall's Tau
    A rank correlation metric that measures the similarity between two rankings by counting the number of concordant and discordant pairs. It ranges from -100% (complete disagreement) to 0% (no correlation) to 100% (complete agreement).
    **Formula:** `(Number of concordant pairs − Number of discordant pairs) / Total pairs`
    