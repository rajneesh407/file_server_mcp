
    This table summarizes the test results for four different user messages that fall outside the scope of credit card inquiries. Each message was run through the pipeline 5 times to evaluate the model's stability and accuracy in providing appropriate, templated responses.

    ##### **Note on Semantic Similarity Calculation**
    For calculating agreement and stability, similarity scores are first converted to a binary result: a score of **0.80 or higher is considered a successful match (1)**, while a score below 0.80 is considered a mismatch (0).

    ##### **Expected Response Template**
    The single expected template for all out-of-scope messages is:
    > "I'm sorry, I can only help with credit card related questions. Please contact customer service for other inquiries."

    ---

    ##### **Scenario Comparison**

    | Metric | Scenario: Weather Query | Scenario: Travel Booking | Scenario: Technical Support | Scenario: General Question |
    | :--- | :--- | :--- | :--- | :--- |
    | **User Message** | "What's the weather today?" | "Book me a flight to NYC" | "My computer won't start" | "What time does the bank close?" |
    | **Example Output** | `I can only help with credit card questions.` | `I can't book flights. I only assist with credit card matters.` | `I can't provide tech support. I only handle credit card inquiries.`|`I don't have bank hours. I only help with credit card questions.`|
    | **Semantic Similarity Scores (5 runs)** | `[1.0, 0.85, 1.0, 0.78, 1.0]` | `[1.0, 0.72, 1.0, 0.68, 1.0]` | `[1.0, 1.0, 1.0, 1.0, 1.0]` | `[1.0, 0.69, 1.0, 0.71, 1.0]` |
    | **Semantic Similarity Agreement**| <span style="color:red">**False**</span> (Binary: [1,1,1,0,1]) | <span style="color:red">**False**</span> (Binary: [1,0,1,0,1]) | <span style="color:green">**True**</span> (Binary: [1,1,1,1,1]) | <span style="color:red">**False**</span> (Binary: [1,0,1,0,1]) |
    | **Answer Relevancy Scores (5 runs)** | `[5, 5, 5, 5, 5]` | `[5, 4, 5, 5, 5]` | `[4, 4, 4, 4, 4]` | `[5, 5, 4, 5, 5]` |
    | **Answer Relevancy Agreement** | <span style="color:green">**True**</span> (5/5 score 5) | <span style="color:red">**False**</span> (4/5 score 5, 1/5 score 4) | <span style="color:green">**True**</span> (5/5 score 4) | <span style="color:red">**False**</span> (4/5 score 5, 1/5 score 4) |
    | **Stable Percentage** | **80%** (majority: score 5) | **80%** (majority: score 5) | **100%** (all score 4) | **80%** (majority: score 5) |

    <br>

    ##### **Overall Summary**

    * **Total Agreement Rate for Semantic Similarity:** **25%** (1 out of 4 scenarios have total agreement)
    * **Total Agreement Rate for Answer Relevancy:** **50%** (2 out of 4 scenarios have total agreement)
    