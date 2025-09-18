
    ##### Accuracy
    Measures the overall correctness of toxicity severity predictions. It is the proportion of messages where the predicted toxicity score exactly matches the target score.
    **Formula:** `(Correct severity predictions) / (Total predictions)`

    ##### Precision
    Measures the quality of toxicity predictions across severity levels (0-4). Uses macro-averaging to treat all severity levels equally, regardless of frequency.
    **Formula:** `Average precision across all severity levels (0, 1, 2, 3, 4)`

    ##### Recall
    Measures how well the model identifies each toxicity severity level. Uses macro-averaging to ensure balanced performance across all severity scores.
    **Formula:** `Average recall across all severity levels (0, 1, 2, 3, 4)`

    ##### F1 Score
    The harmonic mean of precision and recall, providing balanced evaluation across all toxicity severity levels. Particularly useful for imbalanced severity distributions.
    **Formula:** `2 × (Precision × Recall) / (Precision + Recall)`

    ##### Kendall's Tau
    Measures rank correlation between predicted and target severity scores. Evaluates whether the model correctly orders toxicity severity (e.g., score 3 should be more toxic than score 1). Ranges from -100% (complete disagreement) to 100% (perfect ranking agreement).
    **Formula:** `(Concordant pairs - Discordant pairs) / Total pairs`
    