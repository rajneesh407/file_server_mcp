
    ##### Data Flow
    **User Message → 5 Repeated Pipeline Runs → Groundedness Scoring → Stability Metrics Calculation**

    ##### Groundedness Check
    - **Does the question require facts?**
      - ✅ Yes → *Fully Correct / Partial / Not Correct*
      - ❌ No → *Not Applicable*

    ##### Stability Metrics
    - **Total Agreement Rate** = (messages with identical groundedness scores) / (total messages)
    - **Prediction Stability Rate** = (stable majority votes among 5 runs) / (total runs)
    