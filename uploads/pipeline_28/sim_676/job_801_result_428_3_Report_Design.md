
    ##### Data Flow

    **User Message → 5 Repeated Pipeline Runs → Relevancy Scoring → Stability Metrics Calculation**

    ##### Relevancy Check
    - **LLM-as-a-Judge scoring** on a 5-point scale  
      - Scores **4–5 = Accurate**

    ##### Stability Metrics
    - **Total Agreement Rate** = (Messages with identical relevancy scores) / (Total messages)  
    - **Prediction Stability Rate** = (Stable majority votes among 5 runs) / (Total runs)  
    