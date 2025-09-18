
    ##### 🛠️ Implementation Details  
    - Collect stability percentage scores calculated from repeated model responses for each user message categorized by intent  
    - Aggregate these stability scores at the intent level to obtain an overall stability measure per intent  
    - Sort intents from lowest to highest based on their stability measures  
    - Visualize the aggregated stability values as a bar chart, including a red dashed line representing the expected threshold.  

    ##### 📈 Chart Explanation  
    This bar chart displays the **Stability Measure** for each intent category, reflecting how consistently the model produces stable outputs when given identical inputs. Intents are ordered from lowest to highest stability to highlight relative consistency across categories.  

    The **red dashed line** indicates the expected stability threshold, with an annotation showing the exact threshold to facilitate comparison.      
    