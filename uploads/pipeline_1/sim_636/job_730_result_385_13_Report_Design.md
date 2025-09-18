
    ##### 🛠️ Implementation Details
    - Run identical user messages through the model **five times** to evaluate response consistency  
    - Calculate the **stability percentage** for each intent category, representing agreement rate across repeated outputs  
    - Group intents by stability percentage ranges (**0–10%, 10–20%, …**) to analyze distribution of consistency levels  
    - Visualize the percentage of intents within each stability range **alongside the cumulative distribution** for comprehensive insight  

    ##### 📈 Chart Explanation
    The histogram displays how **intent categories are distributed across stability percentage ranges**, reflecting the model’s consistency in generating identical responses to repeated inputs.  
    - The **bars** show the proportion of intents at each stability range  
    - The **cumulative line** shows the total percentage of intents achieving up to a given stability level  
    - Together, they provide a clear view of **overall stability trends**  
    