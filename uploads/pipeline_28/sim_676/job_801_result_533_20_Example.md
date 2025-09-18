
    This document summarizes a robustness test for handling various out-of-scope user messages. Four different non-credit card related queries were tested against five types of linguistic perturbations to evaluate the stability of response template adherence (semantic similarity) and answer relevancy. 🤖

    ---

    #### **Test Scenarios & Expected Response Template**

    The single expected template for all out-of-scope messages is:
    > "I'm sorry, I can only help with credit card related questions. Please contact customer service for other inquiries."

    The user messages tested were:
    * **Weather Query:** "What's the weather like today?"
    * **Travel Booking:** "Can you book a flight for me?"
    * **Technical Support:** "My computer won't start, can you help?"
    * **General Inquiry:** "What time does the bank close?"

    ---

    ### **Perturbation Analysis Results**

    | Perturbation | Weather Query | Travel Booking | Technical Support | General Inquiry |
    | :--- | :--- | :--- | :--- | :--- |
    | **1. Short** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** |
    | **2. Formal** | Similarity: `0.85`<br>Relevancy: **5** | Similarity: `0.72`<br>Relevancy: **4** | Similarity: `0.76`<br>Relevancy: **5** | Similarity: `0.69`<br>Relevancy: **4** |
    | **3. Spelling Errors**| Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** |
    | **4. Synonyms** | Similarity: `0.78`<br>Relevancy: **4** | Similarity: `0.68`<br>Relevancy: **4** | Similarity: `0.73`<br>Relevancy: **5** | Similarity: `0.71`<br>Relevancy: **4** |
    | **5. Expanded** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** | Similarity: `1.0`<br>Relevancy: **5** |

    ---

    ### **Final Stability Calculations**

    #### **Semantic Similarity Stability Results**

    *Note: For stability calculation, similarity scores are converted to a binary result using a threshold of >= 0.80 for a successful match.*

    * **Total Agreement Rate:** **0%**
        * *Explanation:* 0 out of the 4 messages had identical similarity scores across all 5 perturbations.
    * **Stability Percent:** **65%**
        * *Explanation:* The mean of individual message stability scores based on the threshold.
        * **Weather Query:** 80% consensus (4/5 scores >= 0.80)
        * **Travel Booking:** 60% consensus (3/5 scores >= 0.80)
        * **Technical Support:** 60% consensus (3/5 scores >= 0.80)
        * **General Inquiry:** 60% consensus (3/5 scores >= 0.80)

    #### **Answer Relevancy Stability Results**

    * **Total Agreement Rate:** **25%**
        * *Explanation:* Only 1 of the 4 messages (Technical Support) had identical relevancy scores across all 5 perturbations.
    * **Stability Percent:** **75%**
        * *Explanation:* The mean of individual message stability scores.
        * **Weather Query:** 80% consensus (4/5 at score **5**)
        * **Travel Booking:** 60% consensus (3/5 at score **5**)
        * **Technical Support:** 100% consensus (5/5 at score **5**)
        * **General Inquiry:** 60% consensus (3/5 at score **5**)

    ---

    ### **Overall Non-Credit Card Intent Performance**

    * **Average Semantic Similarity:** `0.90`
    * **Template Adherence Rate (Perfect Matches):** `60%`
    * **Average Answer Relevancy:** `4.75 out of 5`
    * **Appropriate Rejection Rate:** `100%`
    