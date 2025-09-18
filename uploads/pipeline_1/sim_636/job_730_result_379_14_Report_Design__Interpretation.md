
    ##### 🛠️ Implementation Details
    - Collect customer utterances representing all intent categories  
    - Assign ground truth labels to each utterance by domain experts  
    - Generate predicted intents from the model for all user messages  
    - Calculate **Accuracy, Precision, Recall, and F1 Score** separately for each intent class  
    - Aggregate these metrics and visualize the results to provide detailed insight into performance across intents  

    ##### 📈 Chart Explanation
    This histogram visualizes the selected performance metric (**Accuracy, Precision, Recall, or F1 Score**) for each intent category.  
    - **Higher bars** → stronger classification performance  
    - **Lower bars** → highlight intents that may require further attention  
    - This format enables quick identification of underperforming intent categories and supports targeted improvements  

    ###### Chart Elements
    - The height of each bar represents the classification performance score for a specific intent category  
    - **Taller bars** → stronger model performance  
    - **Shorter bars** → underperforming intent categories  
    - The chart supports comparing different metrics—**Accuracy, Precision, Recall, F1 Score**—to gain deeper understanding of model behavior  

    ##### 🔑 Key Insights
    - **Consistently high bars** across intents indicate balanced and effective intent classification  
    - **Outlier intents** with significantly lower scores identify targets for further investigation and improvement  
    - **Metric comparisons** help pinpoint specific strengths or gaps in the model’s performance  
    - **Underperforming intents** may require dataset rebalancing or enhanced training data quality  
    