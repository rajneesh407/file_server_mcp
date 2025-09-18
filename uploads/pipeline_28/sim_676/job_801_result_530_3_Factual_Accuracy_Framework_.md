
    ### Evaluation Framework for Fact Retrieval

    This framework categorizes system responses based on the user's intent and the pipeline's performance in retrieving factual information.

    ##### **1. User Messages That Expect Facts**
    *These are queries where the user is explicitly or implicitly asking for factual information.*

    | Pipeline Behavior | Evaluation Category | Description |
    | :--- | :--- | :--- |
    | **Retrieved Facts (As Expected)** | `Fully Correct` | Facts referenced by the model are identical to facts from the database. |
    | | `Partially Correct` | Some facts are correct, while others are incorrect or missing. |
    | | `Not Correct` | Facts referenced are incorrect or do not match the database. |
    | **Failed to Retrieve Facts (Failure)** | `No Fact Retrieved` | No factual information was provided when it was expected. |

    ##### **2. User Messages That Do Not Expect Facts**
    *These are conversational or instructional queries (e.g., "Can you help me with card activation?").*

    | Pipeline Behavior | Evaluation Category | Description |
    | :--- | :--- | :--- |
    | **Retrieved Facts (By Mistake)** | `Retrieved Fact Not Required Mistake` | Unnecessary factual information was provided. |
    | **No Fact Retrieved (As Expected)**| `No Fact Retrieved` | Correctly did not provide unnecessary facts. |
    