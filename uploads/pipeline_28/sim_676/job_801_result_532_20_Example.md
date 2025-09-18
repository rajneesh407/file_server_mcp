
    This document summarizes a robustness test for the "Activate Card" intent. Four user messages (two requiring facts, two not) were tested against five different types of linguistic perturbations to evaluate the stability of factual accuracy and answer relevancy.

    ##### **Test Scenarios & Database Context**

    | Stage | Message 1 (Requires Fact) | Message 2 (Requires Fact) | Message 3 (No Fact) | Message 4 (No Fact) |
    | :--- | :--- | :--- | :--- | :--- |
    | **User Message**| "I need to activate my credit card ending in 4567" | "What's the status of my replacement card activation?" | "Can you help me with card activation?" | "How do I activate my card?" |
    | **Database Facts**| Card: `*4567`<br>Status: `Pending Activation` | Replacement Card: `*8901`<br>Status: `Ready` | N/A - General inquiry | N/A - Process inquiry |

    ---

    ##### **Perturbation Analysis Results**

    | Perturbation | Message 1 (Requires Fact) | Message 2 (Requires Fact) | Message 3 (No Fact) | Message 4 (No Fact) |
    | :--- | :--- | :--- | :--- | :--- |
    | **1. Short** | Facts: `Fully Correct`<br>Relevancy: **4** | Facts: `Fully Correct`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** |
    | **2. Formal** | Facts: `Partially Correct`<br>Relevancy: **3** | Facts: `Fully Correct`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** |
    | **3. Spelling Errors**| Facts: `Fully Correct`<br>Relevancy: **4** | Facts: `Fully Correct`<br>Relevancy: **4** | Facts: `No Fact Retrieved`<br>Relevancy: **4** | Facts: `No Fact Retrieved`<br>Relevancy: **5** |
    | **4. Synonyms** | Facts: `Fully Correct`<br>Relevancy: **4** | Facts: `Fully Correct`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** |
    | **5. Expanded** | Facts: `Fully Correct`<br>Relevancy: **4** | Facts: `Fully Correct`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **5** | Facts: `No Fact Retrieved`<br>Relevancy: **4** |

    ---

    #### **Final Stability Calculations**

    ##### **Factual Accuracy Stability Results**

    * **Total Agreement Rate:** **75%**
        * *Explanation:* 3 out of the 4 messages had identical factual accuracy results across all 5 perturbations.
    * **Stability Percent:** **95%**
        * *Explanation:* The mean of individual message consensus scores.
        * **Message 1:** 80% consensus (4/5 `Fully Correct`)
        * **Message 2:** 100% consensus (5/5 `Fully Correct`)
        * **Message 3:** 100% consensus (5/5 `No Fact Retrieved`)
        * **Message 4:** 100% consensus (5/5 `No Fact Retrieved`)

    ##### **Answer Relevancy Stability Results**

    * **Total Agreement Rate:** **0%**
        * *Explanation:* 0 out of the 4 messages had identical relevancy scores across all 5 perturbations.
    * **Stability Percent:** **80%**
        * *Explanation:* The mean of individual message consensus scores.
        * **Message 1:** 80% consensus (4/5 at score **4**)
        * **Message 2:** 80% consensus (4/5 at score **5**)
        * **Message 3:** 80% consensus (4/5 at score **5**)
        * **Message 4:** 80% consensus (4/5 at score **5**)
    