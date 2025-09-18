
    This table summarizes the test results for four different user messages related to the "Activate Card" intent. Each message was run through the pipeline 5 times to evaluate the stability and accuracy of the responses.

    ##### **Scenario Comparison**

    | Metric | Scenario: Requires Fact 1 | Scenario: Requires Fact 2 | Scenario: No Fact 1 | Scenario: No Fact 2 |
    | :--- | :--- | :--- | :--- | :--- |
    | **User Message** | "What's my card number for activation?" | "When does my new card expire?" | "Can you help me with card activation?" | "How do I activate my credit card?" |
    | **Example Output** | `Card ending in 4567, CVV required` | `Expires 12/2027` | `Call 1-800-XXX or use online banking` | `You can activate by phone or online` |
    | **Factual Accuracy (5 runs)** | `[FC, FC, PC, FC, FC]` | `[FC, FC, FC, FC, FC]` | `[FC, FC, FC, FC, FC]` | `[FC, FC, NC, FC, FC]` |
    | **Factual Accuracy Agreement**| <span style="color:red">**False**</span> (4/5 FC, 1/5 PC) | <span style="color:green">**True**</span> (5/5 FC) | <span style="color:green">**True**</span> (5/5 FC) | <span style="color:red">**False**</span> (4/5 FC, 1/5 NC) |
    | **Answer Relevancy Scores (5 runs)** | `[5, 5, 4, 5, 5]` | `[5, 5, 5, 5, 5]` | `[4, 5, 4, 4, 4]` | `[5, 5, 5, 5, 5]` |
    | **Answer Relevancy Agreement** | <span style="color:red">**False**</span> (4/5 score 5, 1/5 score 4) | <span style="color:green">**True**</span> (5/5 score 5) | <span style="color:red">**False**</span> (4/5 score 4, 1/5 score 5) | <span style="color:green">**True**</span> (5/5 score 5) |
    | **Stable Percentage** | **80%** (majority: score 5) | **100%** (all score 5) | **80%** (majority: score 4) | **100%** (all score 5) |
    <br>
    ##### **Legend for Factual Accuracy Values**
    * **FC**: `Fully Correct`
    * **PC**: `Partially Correct`
    * **NC**: `Not Correct`<br>

    ##### **Overall Summary**

    * **Total Agreement Rate for Factual Accuracy:** **50%** (2 out of 4 scenarios have total agreement)
    * **Total Agreement Rate for Answer Relevancy:** **50%** (2 out of 4 scenarios have total agreement)
    