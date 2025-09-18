
    ##### Data Process Steps
    1. Filter questions **NOT** requiring credit card facts  
    2. Submit user question + LLM response to judge model  
    3. Judge scores relevancy on a 1–5 scale  
    4. Group scores by intent classification  
    5. Calculate percentage distribution per score level  

    ##### Visualization Design
    - **Stacked bar chart** showing relevancy score distribution for general credit card questions  
    - These questions should typically perform well since they **don’t require specific fact retrieval**  
    