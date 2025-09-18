
    #### Box-Plot Elements
    * **X-axis:** Toxicity metric dimensions (Contains Prohibited Words, Toxicity, Obscenity, Identity Attack, Insult, Threat, Sarcasm).
    * **Y-axis:** Toxicity scores assigned by an LLM Judge for user input (red) and pipeline response (green) on a scale from 0 (non-toxic) to 4 (highly toxic).
    * **Vertical Spread:** Shows the range and variability of toxicity scores for each metric dimension before and after pipeline processing.

    #### 🔑 Key Insight
    The wide distributions with higher toxicity scores in user input indicate a substantial presence of toxic content. In contrast, the conversational AI responses cluster tightly near zero, illustrating strong detoxification effectiveness across all metrics.
    