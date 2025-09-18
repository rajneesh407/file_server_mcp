
    ### Implementation Details
    1. **Prepare Data**: The function starts by converting the `target_score` and `predicted_score` columns into categorical string labels. This ensures clarity when comparing across discrete score values.
    2. **Construct Matrix**: A cross-tabulation (`pd.crosstab`) is used to create a two-dimensional contingency table of counts, mapping the distribution of predictions (`Predicted Score`) against ground-truth labels (`Target Score (Actual)`).
    3. **Normalize & Style**: A custom color scale (from deep purple to bright yellow) is applied to visually distinguish low vs. high counts. Values are bounded between 0 and the maximum observed cell count for consistent color intensity.
    4. **Annotate Counts**: Each heatmap cell is overlaid with its raw count, dynamically switching the annotation color (black or white) to maximize readability depending on background intensity.
    5. **Finalize Layout**: Titles, axis labels, margins, and a consistent template are applied for a clean, professional look. The heatmap is interactive, allowing zooming and hover exploration.

    ### Chart Explanation
    This heatmap provides a **matrix view of prediction accuracy** by comparing **Target Scores (Actual)** (rows) against **Predicted Scores** (columns).
    - **Diagonal cells** represent correct predictions (where target = predicted).
    - **Off-diagonal cells** indicate misclassifications, with higher counts highlighting systematic errors.
    - The **color intensity** reflects the relative frequency of each prediction-target pairing.
    - Overlaid **numeric annotations** provide exact counts, ensuring both macro (pattern spotting) and micro (raw value) insights.

    This visualization helps quickly identify whether misclassifications are random or concentrated in particular score ranges, giving direct guidance for model calibration and error analysis.
    