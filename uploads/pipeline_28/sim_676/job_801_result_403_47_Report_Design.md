
    ##### <span style="color:#1f77b4;">🛠️ Data Process Steps</span><br>
    • Filter user messages requiring factual data
    • Check if facts were retrieved from RAG system
    • Extract facts used in LLM responses
    • Compare with source fact database
    • Score as Fully Correct, Partial Correct, or Not Correct
    • Aggregate by intent category

    ##### <span style="color:#1f77b4;">📈 Chart Explanation</span><br>
    This stacked bar chart shows the distribution of **groundedness scores** across different credit card intent categories. Only questions that **require factual data AND have retrieved facts from the RAG system** are included in this analysis.<br>

    ##### <span style="color:#1f77b4;">🔎 How to Read This Chart</span><br>
    Higher percentages of **"Fully Correct" (green)** indicate better factual accuracy.
    **"Partial Correct" (yellow)** suggests some facts are accurate but others are missing or incorrect.
    **"Not Correct" (red)** indicates significant factual errors.<br>
    