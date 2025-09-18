
    This chart presents an analysis of toxicity scores by user intent for utterances identified as toxic. It highlights the system’s ability to handle various intents without generating toxicity in its responses for the selected category.

    ##### 🛠️ Implementation Details
    * **Approach:** An LLM configured as a Judge evaluates pipeline response toxicity for distinct user intents within toxic utterances. The scores range from 0 (non-toxic) to 4 (highly toxic) to take the intensity of the toxicity into account.
    * **Strength:** Enables pinpointing of any potential intent-specific toxicity issues in system outputs, ensuring robust moderation across varied user requests.

    ##### 📈 Chart Explanation
    The boxplot chart should display near-zero toxicity scores across all intents, demonstrating the system’s effective mitigation of toxicity even when responding to toxic user messages.
    