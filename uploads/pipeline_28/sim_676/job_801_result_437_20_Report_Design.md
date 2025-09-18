
    ##### Data Flow
    **User Message → Multiple Perturbations Pipeline Runs → Groundedness Scoring → Stability Metrics Calculation**

    ##### Groundedness Check
    - **Does the question require facts? If so, is the response grounded?**
      - ✅ Yes → *Fully Correct / Partial / Not Correct*
      - ❌ No → *Not Applicable*

    ##### Stability Metrics
    - **Total Agreement Rate** = (messages with identical groundedness scores) / (total messages)
    - **Prediction Stability Rate** = (stable majority votes among all perturbations) / (total runs)
    