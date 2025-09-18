
    This chart presents a distribution analysis revealing how toxicity is effectively reduced from non-toxic user queries to AI responses across multiple toxicity dimensions.

    ##### 🛠️ Implementation Details
    * **Approach:** The system leverages an LLM acting as a Judge to score toxicity levels for both user messages and corresponding AI-generated responses. The scores range from 0 (non-toxic) to 4 (highly toxic) to take the intensity of the toxicity into account.
    * **Toxicity Dimensions Analyzed:** Contains Prohibited Words, Toxicity, Obscenity, Identity Attack, Insult, Threat, and Sarcasm.
    * **Strength:** The LLM’s advanced contextual understanding allows nuanced differentiation of toxicity before and after content processing.

    ##### 📈 Chart Explanation
    The box-plots depict broad toxicity score distributions (red) in user messages that should narrow sharply towards zero (green) in pipeline responses, illustrating strong toxicity mitigation effectiveness.
    