
    ##### 🛠️ Implementation Details
    1. **Collect Metrics**: The function ingests a pandas DataFrame containing pre-calculated performance scores (`Accuracy`, `Precision`, `Recall`, `F1-Score`, `Kendall's Tau`) for various intents.
    2. **Process Data**: It filters out the "Overall" aggregate row to focus purely on individual intent performance.
    3. **Sort Intents**: For each metric selected, the intents are sorted in ascending order (from lowest to highest score) to immediately highlight the poorest-performing categories.
    4. **Visualize**: An interactive bar chart is generated using Plotly. A separate bar trace is created for each metric, with only one being visible at a time. A configurable red dashed line is added to represent the target performance threshold.

    ##### 📈 Chart Explanation
    This interactive bar chart visualizes key performance metrics for different intent categories. The dropdown menu allows you to select a metric (e.g., **Accuracy**, **F1-Score**) to display.
    Intents are always ordered from **lowest to highest** performance for the selected metric, making it easy to identify areas needing improvement. The bars are annotated with their exact percentage values for precision.
    The **red dashed line** represents the minimum acceptable performance threshold, providing a quick visual reference to see which intents meet the target and which fall short.
    