
    ##### Data Flow 📊

    **User Message → Multiple Perturbed Pipeline Runs → Groundedness & Relevancy Scoring → Stability Metrics Calculation**

    ### Accuracy Checks ✅

    * **Groundedness Scoring:**
        * LLM-as-a-Judge scores on a 5-level scale (Very High, High, Medium, Low, Very Low).
        * Scores of **Very High** or **High** are considered accurate.

    ##### Stability Metrics ⚖️

    * **Total Agreement Rate** = (Number of messages with identical scores across all perturbations) / (Total messages)
    * **Prediction Stability Rate** = (Number of majority vote scores among perturbations) / (Total perturbations)
    