
    ##### 📊 Chart Elements
    - **Bars**: Represent the performance score percentage (e.g., Accuracy, F1-Score) for each individual intent category.
    - **Horizontal Sorting**: Intents are sorted along the x-axis from the lowest to the highest performance score, immediately highlighting the weakest areas.
    - **Threshold Line**: The red dashed horizontal line indicates the minimum acceptable performance target, providing a clear pass/fail benchmark.
    - **Numeric Labels**: Precise percentage scores are displayed directly on each bar for detailed evaluation.

    ##### 🔑 Key Insights
    - **Identify Underperformers**: The intents appearing on the far left are the primary candidates for review, as they have the lowest scores for the selected metric. Any intent falling below the red threshold line requires immediate attention.
    - **Diagnose Error Types**: By switching between metrics, you can understand the nature of the model's failures. For example, an intent with low **Precision** might be over-triggering incorrectly, while one with low **Recall** may not be firing when it should.
    - **Confirm Strong Performance**: Intents consistently appearing on the right side of the chart across all metrics are performing robustly and can be considered reliable.
    