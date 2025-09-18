
    For user messages that are credit card-related, an LLM-as-a-judge model produces a score from 1 to 5 to evaluate if the response addresses the user's query in an expected way. By repeating the same user message 5 times, we test the **stability** of the answer relevancy score, which is measured by the total agreement rate and the percentage of stable runs.

    ##### **Answer Relevancy Scoring Scale**

    | Score | Description |
    | :---: | :--- |
    | **5** | **Perfectly relevant** and addresses all aspects of the user query. |
    | **4** | **Highly relevant** with minor gaps. |
    | **3** | **Moderately relevant** but missing some key aspects. |
    | **2** | **Somewhat relevant** but with significant gaps. |
    | **1** | **Not relevant** or completely off-topic. |

    **Note on Stability:** Stability is measured by the consistency of these scores across the 5 repeated runs for each user message. A higher consistency indicates a more stable and reliable response generation process.
    