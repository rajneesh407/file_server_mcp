
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Faithfulness Testing Process Report</title>
    <style>
        body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
            background-color: #f0f8ff; /* Light blue background */
            margin: 0;
            padding: 1rem;
        }
        @media (min-width: 768px) {
            body {
                padding: 2rem;
            }
        }
        .report-container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 2rem;
            border-radius: 0.75rem;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: 1px solid #cce5ff;
        }
        .header {
            text-align: center;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid #e5e7eb;
            margin-bottom: 1.5rem;
        }
        .header h1 {
            font-size: 1.875rem;
            font-weight: 700;
            color: #003366;
            margin: 0;
        }
        .header p {
            font-size: 1rem;
            color: #6b7280;
            margin-top: 0.5rem;
        }
        .step-section {
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .step-section:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        .step-title {
            color: #004085;
            font-weight: 600;
            font-size: 1.25rem;
            margin-bottom: 1rem;
        }
        .section-description {
            color: #4b5563;
            margin-bottom: 1rem;
        }
        .section-subtitle {
            font-weight: 600;
            color: #374151;
            margin-bottom: 0.5rem;
            margin-top: 1.5rem;
        }
        .section-subtitle:first-child {
            margin-top: 0;
        }
        .user-message, .llm-response, .code-block {
            background-color: #f1f5f9;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .user-message {
            border-left: 4px solid #3b82f6;
            font-style: italic;
            color: #475569;
        }
        .llm-response {
            border-left: 4px solid #14b8a6;
            color: #475569;
        }
        .code-block {
            font-family: monospace;
            font-size: 0.875rem;
            white-space: pre-wrap;
            word-break: break-all;
            color: #334155;
        }
        .styled-list {
            list-style-type: disc;
            list-style-position: inside;
            color: #374151;
            padding-left: 0;
        }
        .styled-list li {
            margin-bottom: 0.5rem;
        }
        .note {
            font-size: 0.875rem;
            color: #6b7280;
            margin-top: 1rem;
        }
        .status-passed {
            color: #16a34a;
            font-weight: 700;
        }
        .confidence-high {
            font-weight: 700;
            color: #16a34a;
        }
        .final-result {
            background-color: #d1fae5;
            border: 1px solid #a7f3d0;
            color: #065f46;
            padding: 1.5rem;
            border-radius: 0.5rem;
            text-align: center;
            margin-top: 1.5rem;
        }
        .final-result h2 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-top: 0;
            margin-bottom: 0.5rem;
        }
        .final-result p {
            margin: 0;
            font-size: 1.125rem;
        }
    </style>
    </head>
    <body>
    <div class="report-container">
        <div class="header">
            <h1>Complete Faithfulness Testing Process</h1>
            <p>A step-by-step pipeline from user input to fact verification for Customer ID C008.</p>
        </div>
        <div class="step-section">
            <h2 class="step-title">Step 1: Evaluation Data Selection</h2>
            <p class="section-description">The process begins with the user's query, which is direct and requires a fast, factual response.</p>
            <h3 class="section-subtitle">User Message:</h3>
            <div class="user-message">
                <p>"I don't have time for this, just tell me which cards has no annual fee and stop wasting my time."</p>
            </div>
            <p class="note"><strong>Note:</strong> The message from <strong>Henry Adams (C008)</strong> is identified as an urgent request for specific, factual card information.</p>
        </div>
        <div class="step-section">
            <h2 class="step-title">Step 2: Intent Classification Pipeline</h2>
            <p class="section-description">The system correctly classifies the user's request to find and compare cards with no annual fees.</p>
            <ul class="styled-list">
                <li><strong>Classified Intent:</strong> Checking Annual Fees</li>
                <li><strong>Sub-intent:</strong> Comparing fees across card types</li>
                <li><strong>Classification Confidence:</strong> <span class="confidence-high">High</span></li>
            </ul>
        </div>
        <div class="step-section">
            <h2 class="step-title">Step 3: SQL Query Generation & Database Retrieval</h2>
            <p class="section-description">A specific SQL query is generated to fetch only the cards belonging to the customer that have a zero annual fee.</p>
            <h3 class="section-subtitle">Generated SQL Query:</h3>
            <div class="code-block">SELECT T1.*, T2.*
    FROM   customers AS T1 LEFT JOIN cards AS T2 ON T1.customer_id = T2.customer_id
    WHERE  T1.customer_id = 'C008' AND ( T2.annual_fee = 0 );</div>
            <h3 class="section-subtitle">Retrieved Database Records:</h3>
            <div class="code-block">[
    {
    "customer_id": "C008",
    "name": "Henry Adams",
    "cards": [
      {
        "card_number": "4000-9876-5432-1098",
        "card_type": "MASTERCARD",
        "status": "BLOCKED",
        "annual_fee": 0
      },
      {
        "card_number": "4000-1111-2222-3333",
        "card_type": "VISA",
        "status": "ACTIVE",
        "annual_fee": 0
      }
    ]
    }
    ]</div>
        </div>
        <div class="step-section">
            <h2 class="step-title">Step 4: LLM Response Generation</h2>
            <p class="section-description">The LLM processes the retrieved data to generate a concise answer and extracts the key facts for verification.</p>
            <h3 class="section-subtitle">Textual Response:</h3>
            <div class="llm-response">
                <p>"You have two cards with no annual fee: your MASTERCARD ending in 1098 and your VISA card ending in 3333."</p>
            </div>
            <h3 class="section-subtitle">Associated Facts List:</h3>
            <div class="code-block">[
    {
    "fact": "MASTERCARD ending in 1098",
    "data_path": "cards.0.card_type",
    "referenced_value": "MASTERCARD"
    },
    {
    "fact": "ending in 1098",
    "data_path": "cards.0.card_number", 
    "referenced_value": "4000-9876-5432-1098"
    },
    {
    "fact": "VISA card ending in 3333",
    "data_path": "cards.1.card_type",
    "referenced_value": "VISA"
    },
    {
    "fact": "ending in 3333",
    "data_path": "cards.1.card_number",
    "referenced_value": "4000-1111-2222-3333"
    }
    ]</div>
        </div>
        <div class="step-section">
            <h2 class="step-title">Step 5: Assessment & Fact Correctness Detection</h2>
            <p class="section-description">Each fact stated in the response is automatically cross-referenced with the ground-truth data from the database.</p>
            <div class="code-block">[
    {
        "fact": "MASTERCARD ending in 1098",
        "data_path": "cards.0.card_type",
        "expected_value": "MASTERCARD",
        "retrieved_value": "MASTERCARD",
        "status": "<span class='status-passed'>PASSED</span>",
        "reason": "The retrieved value matches the expected value."
    },
    {
        "fact": "ending in 1098",
        "data_path": "cards.0.card_number",
        "expected_value": "4000-9876-5432-1098",
        "retrieved_value": "4000-9876-5432-1098",
        "status": "<span class='status-passed'>PASSED</span>",
        "reason": "The retrieved value matches the expected value."
    },
    {
        "fact": "VISA card ending in 3333",
        "data_path": "cards.1.card_type",
        "expected_value": "VISA",
        "retrieved_value": "VISA",
        "status": "<span class='status-passed'>PASSED</span>",
        "reason": "The retrieved value matches the expected value."
    },
    {
        "fact": "ending in 3333",
        "data_path": "cards.1.card_number",
        "expected_value": "4000-1111-2222-3333",
        "retrieved_value": "4000-1111-2222-3333",
        "status": "<span class='status-passed'>PASSED</span>",
        "reason": "The retrieved value matches the expected value."
    }
    ]</div>
        </div>
        <div class="final-result">
            <h2>Final Result</h2>
            <p><strong>Faithfulness Score: 1 (True)</strong></p>
            <p>All facts were verified successfully. The response is faithful to the source data.</p>
        </div>
    </div>
    </body>
    </html>
    