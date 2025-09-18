
    For user messages that are not credit card-related, an LLM-as-a-judge model evaluates if the response appropriately addresses the query, which typically means correctly redirecting the user. The model assigns a relevancy score from 1 to 5. By repeating the same user message 5 times, we test the **stability** of this score (measured by total agreement rate and percentage stable).

    ##### **Answer Relevancy Scoring Scale**

    | Score | Description |
    | :---: | :--- |
    | **5** | **Perfectly relevant** redirect message. |
    | **4** | **Highly relevant** with minor gaps in the redirect messaging. |
    | **3** | **Moderately relevant** but provides an inconsistent redirect. |
    | **2** | **Somewhat relevant** but provides an unclear redirect. |
    | **1** | **Not relevant** or an incorrect response type. |

    **Note on Stability:** Stability is measured by the consistency of these scores across the 5 repeated runs for each user message. This ensures the model's behavior in handling and redirecting non-credit card queries is reliable.
    