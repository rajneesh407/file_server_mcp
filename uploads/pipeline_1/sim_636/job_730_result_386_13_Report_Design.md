
    ##### 🛠️ Implementation Details
    - Collect agreement rate metrics for individual utterances grouped by intent category.  
    - Aggregate these metrics at the intent level to obtain total agreement rates per intent.  
    - Sort intent categories in ascending order based on **Total Agreement Rate**.  
    - Visualize the aggregated agreement rates as a bar chart, including a expected threshold reference line.  

    ##### 📈 Chart Explanation
    This bar chart illustrates the total agreement rate for each intent category, showing how consistently the model produces stable outputs within each intent.  

    - Intents are arranged from **lowest to highest agreement rate** to highlight relative performance differences.  
    - The **red dashed line** indicates the expected threshold for agreement rate.  
    - An **annotation** displays the exact expected threshold percentage value for easy comparison.  
    