
    ### Chart Elements
    - **Heatmap Cells**: Each cell represents the count of records for a specific combination of **Target Score (Actual)** (row) and **Predicted Score** (column).
    - **Color Intensity**: Darker shades correspond to higher counts, making it easy to spot areas with concentrated predictions.
    - **Diagonal Line**: Cells along the diagonal (where Target = Predicted) represent correct predictions.
    - **Numeric Annotations**: Exact counts are displayed within each cell, ensuring transparency and enabling precise evaluation.
    - **Axes**:
      - **Y-Axis** → Target Score (Actual)
      - **X-Axis** → Predicted Score

    ### Key Insights
    - **Accuracy Patterns**: A strong diagonal pattern indicates the model is predicting correctly most of the time. Sparse or weak diagonals suggest widespread misclassification.
    - **Error Concentration**: Off-diagonal clusters highlight systematic errors. For example, if many `Target = 3` cases are predicted as `Predicted = 2`, it indicates the model consistently underestimates that score.
    - **Rare vs. Frequent Labels**: Brighter areas along a particular row or column reveal which target or predicted scores dominate the dataset.
    - **Balanced vs. Biased Predictions**: If certain predicted score columns are consistently darker, it suggests the model is biased toward predicting those scores regardless of the actual target.
    