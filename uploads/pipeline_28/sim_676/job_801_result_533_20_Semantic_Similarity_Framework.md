
    This framework evaluates how consistently the model adheres to a standard template when responding to user messages that are not related to credit cards. 🤖

    ##### **Expected Response Template**

    For all out-of-scope inquiries, the model is expected to generate a response that is semantically equivalent to the following template:

    > "I'm sorry, I can only help with credit card related questions. Please contact customer service for other inquiries."


    ##### **Semantic Similarity Scoring**

    The consistency of the model's output is measured by calculating the semantic similarity between the actual response and the expected template. The scores are categorized as follows:

    | Score / Category | Description |
    | :--- | :--- |
    | **1.0** (Perfect Match) | The response exactly matches the template word-for-word. |
    | **0.8 - 0.99** (High Similarity) | The response is semantically very similar, with only minor, inconsequential phrasing differences. |
    | **0.6 - 0.79** (Moderate Similarity)| The response conveys the core message but is structured differently or omits some details. |
    | **< 0.6** (Low Similarity) | The response deviates significantly in meaning or fails to redirect the user appropriately. |
    