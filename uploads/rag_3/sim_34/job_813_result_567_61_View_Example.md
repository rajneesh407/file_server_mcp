
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RAG Pipeline Testing Report</title>
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
            .user-message, .code-block {
                background-color: #f1f5f9;
                padding: 1rem;
                border-radius: 0.5rem;
            }
            .user-message {
                border-left: 4px solid #3b82f6;
                font-style: italic;
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
            .final-result {
                background-color: #d1fae5;
                border: 1px solid #a7f3d0;
                color: #065f46;
                padding: 1.5rem;
                border-radius: 0.5rem;
                margin-top: 1.5rem;
            }
            .final-result h2 {
                font-size: 1.5rem;
                font-weight: 700;
                margin-top: 0;
                margin-bottom: 0.5rem;
                text-align: center;
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
                <h1>Comprehensive Example: RAG Pipeline Testing</h1>
                <p>Complete Test Case for Customer ID C013.</p>
            </div>
            <div class="step-section">
                <h2 class="step-title">Test Case Details</h2>
                <ul class="styled-list">
                    <li><strong>Customer ID:</strong> C013</li>
                    <li><strong>Intent:</strong> Card Activation</li>
                    <li><strong>Sub-Intent:</strong> With Credit Card First 4</li>
                    <li><strong>Expected DB Call:</strong> <span style="font-weight: bold; color: #16a34a;">Yes</span></li>
                    <li><strong>Predicted DB Call:</strong> <span style="font-weight: bold; color: #16a34a;">Yes</span></li>
                    <li><strong>Fact Correctness:</strong> <span style="font-weight: bold; color: #16a34a;">Exact Match</span></li>
                </ul>
            </div>
            <div class="step-section">
                <h2 class="step-title">User Message</h2>
                <div class="user-message">
                    <p>"Hello, I just got my new card and it starts with 5400, I'm not in urgent rush but could you please help activate it when you have a moment? Thank you."</p>
                </div>
            </div>
            <div class="step-section">
                <h2 class="step-title">Retrieval Stage: SQL Generation & Execution</h2>
                <h3 class="section-subtitle">Generated SQL Query:</h3>
                <div class="code-block">SELECT T1.*, T2.*
    FROM   customers AS T1 LEFT JOIN cards AS T2 ON T1.customer_id = T2.customer_id
    WHERE  T1.customer_id = :cid AND ( T2.card_number LIKE '5400%' );</div>
                <h3 class="section-subtitle">Retrieved DB Record:</h3>
                <div class="code-block">[
      {
        "customer_id": "C013",
        "name": "Maria Silva",
        "phone": "+55-11-91234-5678",
        "region": "BR",
        "cards": [
          {
            "card_number": "5400-1111-2222-3333",
            "card_type": "VISA",
            "status": "ACTIVE",
            "intl_usage": true,
            "usage_limit": 300,
            "current_balance": 150,
            "annual_fee": 25,
            "maximum_limit": 10000,
            "service_requests": []
          }
        ]
      }
    ]</div>
            </div>
            <div class="step-section">
                <h2 class="step-title">Verification: Comparing Retrieved vs. Expected</h2>
                 <h3 class="section-subtitle">Expected Facts:</h3>
                <div class="code-block">[
      {
        "customer_id": "C013",
        "name": "Maria Silva",
        "phone": "+55-11-91234-5678",
        "region": "BR",
        "cards": [
          {
            "card_number": "5400-1111-2222-3333",
            "card_type": "VISA",
            "status": "ACTIVE",
            "intl_usage": true,
            "usage_limit": 300,
            "current_balance": 150,
            "annual_fee": 25,
            "maximum_limit": 10000,
            "service_requests": []
          }
        ]
      }
    ]</div>
            </div>
            <div class="final-result">
                <h2>Analysis</h2>
                <p>This represents a successful <strong>exact match</strong> where the system correctly identified the need for a database call, generated an appropriate SQL query to find the card starting with "5400", and retrieved the precise customer and card information expected.</p>
            </div>
        </div>
    </body>
    </html>
    