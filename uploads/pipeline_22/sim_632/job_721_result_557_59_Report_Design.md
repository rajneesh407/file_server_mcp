
    ##### Data Flow

    **User Message → 5 Repeated Pipeline Runs → Groundedness Scoring → Stability Metrics Calculation**

    ##### Groundedness Check
    - **LLM-as-a-Judge scoring** on a 5-level confidence scale (Very High, High, Medium, Low, Very Low)
      - Scores **High / Very High = Accurate**

    ##### Stability Metrics
    - **Total Agreement Rate** = (Messages with identical groundedness scores) / (Total messages)
    - **Prediction Stability Rate** = (Stable majority votes among 5 runs) / (Total runs)
    