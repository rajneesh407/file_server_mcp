
    This framework outlines the evaluation criteria for factual accuracy based on whether a credit card-related query expects a fact-based response.

    ##### **i. User Messages That Expect Facts**
    These are queries where the user is asking for specific information that should be retrieved from a database.

    * **If the pipeline retrieved facts (As Expected):**
        * `Fully Correct`: Facts referenced by the model are identical to the facts from the database.
        * `Partially Correct`: Some facts match, but others are missing or incorrect.
        * `Not Correct`: Facts referenced do not match the database facts.

    * **If the pipeline failed to retrieve facts (Failure):**
        * `No Fact Retrieved`: The pipeline did not return the expected factual data.


    ##### **ii. User Messages That Do Not Expect Facts**
    *(e.g., "Can you help me with card activation?")*

    These are queries that are conversational or require general instructions, not specific user data.

    * **If the pipeline retrieved facts (By Mistake):**
        * `Retrieved Fact Not Required Mistake`: The pipeline incorrectly returned factual data when none was needed.

    * **If no facts were retrieved (As Expected):**
        * `No Fact Retrieved`: The pipeline correctly did not return factual data.
    