
    ##### Data Flow 📊

    **User Message → Multiple Perturbed Pipeline Runs → Groundedness & Relevancy Scoring → Stability Metrics Calculation**

    ##### Accuracy Checks ✅

    * **Answer Relevancy Scoring:**
        * LLM-as-a-Judge scoring on a 5-point scale.
        * Scores **4–5** are considered accurate.

    ##### Stability Metrics ⚖️

    * **Total Agreement Rate** = (Number of messages with identical scores across all perturbations) / (Total messages)
    * **Prediction Stability Rate** = (Number of majority vote scores among perturbations) / (Total perturbations)
    