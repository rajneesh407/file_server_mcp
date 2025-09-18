
    ##### 🛠️ Implementation Details
    - Run identical user messages through the model **five times** to assess response consistency  
    - Calculate the **stability percentage (agreement rate)** for each intent category based on repeated outputs  
    - Group intents into ranges of total agreement rates (**0–10%, 10–20%, …**) to analyze distribution  
    - Visualize the percentage of intents within each agreement rate range **alongside a cumulative percentage line** showing overall coverage  

    ##### 📈 Chart Explanation
    This histogram displays the **distribution of intent categories by their stability percentage ranges**, showing how consistently the model produces the same output for repeated inputs.  
    - The **bars** represent the proportion of intents in each agreement rate range  
    - The **cumulative line** highlights the progressive total percentage of intents achieving at least a given agreement rate  
    