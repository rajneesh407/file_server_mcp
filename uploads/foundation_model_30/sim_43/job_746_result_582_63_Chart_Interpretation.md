
    ### Chart Elements
    - **Bars**: Represent the performance score percentage (e.g., Accuracy, F1-Score) for each individual toxicity category.
    - **Horizontal Sorting**: Categories are sorted along the x-axis from the lowest to the highest performance score, immediately highlighting the weakest areas.
    - **Threshold Line**: The red dashed horizontal line indicates the minimum acceptable performance target, providing a clear pass/fail benchmark.
    - **Numeric Labels**: Precise percentage scores are displayed directly on each bar for detailed evaluation.

    ### Key Insights
    - **Identify Underperformers**: The toxicity categories appearing on the far left are the primary candidates for review, as they have the lowest scores for the selected metric. Any category falling below the red threshold line requires immediate attention.
    - **Diagnose Error Types**: By switching between metrics, you can understand the nature of the model's failures. For example, a category with low **Precision** might be over-flagging content incorrectly, while one with low **Recall** may not be detecting harmful content when it should.
    - **Confirm Strong Performance**: Categories consistently appearing on the right side of the chart across all metrics are performing robustly and can be considered reliable for content moderation.
    