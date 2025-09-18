
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Executive Summary - Accuracy</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100%;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                background-color: #ffffff;
                color: #5a626a;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            .content-wrapper {
                width: 100%;
                margin: 0;
                padding: 2rem 3rem;
                box-sizing: border-box;
            }
            h1, h2, h3, h4 {
                color: #212529;
                font-weight: 600;
                margin: 0;
            }
            h1 {
                font-size: 2rem;
                margin-bottom: 0.25rem;
            }
            h2 {
                font-size: 1.5rem;
                margin-top: 2.5rem;
                margin-bottom: 1rem;
            }
            h3 {
                font-size: 1.15rem;
                margin-bottom: 0.75rem;
            }
            h4 {
                font-size: 1.1rem;
                margin-bottom: 0.5rem;
            }
            p {
                line-height: 1.6;
                margin: 0;
            }
            .subtitle {
                font-size: 1.1rem;
                color: #6c757d;
                margin-bottom: 2rem;
            }
            .flex-container {
                display: flex;
                flex-wrap: wrap;
                gap: 1.5rem;
                margin-top: 1.5rem;
            }
            .flex-container > div {
                flex: 1;
                min-width: 250px;
            }
            .info-box {
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 8px;
                padding: 1.5rem;
            }
            .metric-tag {
                display: inline-block;
                background-color: #e9ecef;
                border: 1px solid #dee2e6;
                padding: 4px 10px;
                border-radius: 12px;
                font-size: 0.8rem;
                margin-top: 10px;
                color: #495057;
            }
            .guide-box {
                background: linear-gradient(145deg, #e7f3ff, #ffffff);
                border: 1px solid #e9ecef;
                border-left-width: 4px;
                border-radius: 6px;
                padding: 1.5rem;
            }
            .guide-box.high-accuracy {
                border-left-color: #28a745;
            }
            .guide-box.low-accuracy {
                border-left-color: #dc3545;
            }
            .guide-box h3 {
                display: flex;
                align-items: center;
                gap: 0.6rem;
                font-weight: 600;
            }
            .high-accuracy h3 { color: #28a745; }
            .low-accuracy h3 { color: #dc3545; }
            .guide-box ul {
                list-style-type: none;
                padding-left: 0;
                margin: 1rem 0 0 0;
            }
            .guide-box li {
                position: relative;
                padding-left: 1.25em;
                margin-bottom: 0.6rem;
            }
            .guide-box li:last-child {
                margin-bottom: 0;
            }
            .guide-box li::before {
                content: '•';
                position: absolute;
                left: 0;
                color: #6c757d;
                font-size: 1.25em;
                line-height: 1;
            }
        </style>
    </head>
    <body>
        <div class="content-wrapper">
            <h1>Executive Summary - Accuracy (Non-Credit Card Intents)</h1>
            <p class="subtitle">Accuracy assessment results for non-credit card related intents.</p>
            <h2>Testing Methodology</h2>
            <p>In this report, we test how well the Large Language Model (LLM) answers questions that are out-of-scope for the given task. In this case, user messages that do not pertain to credit cards.</p>
            <p style="margin-top: 0.5rem;">LLM response accuracy is evaluated on the following dimensions:</p>
            <div class="flex-container">
                <div class="info-box">
                    <h3>Template Adherence Scoring</h3>
                    <p>This evaluates how closely the LLM's response matches the prompt-defined template answer based on semantic similarity, as measured using "cosine similarity" on the vector embeddings of the expected template and the LLM's response. Scores range from 0 to 1, where 1 means the responses are exactly the same in meaning. If the score is 0.8 or higher, we consider the LLM's response accurate.</p>
                     <span class="metric-tag">Template adherence metric</span>
                </div>
                <div class="info-box">
                    <h3>Answer Relevancy Scoring</h3>
                    <p>Using an LLM-as-judge, score all LLM responses on a 5-point scale measuring response relevance to user messages. Scores ranging from 1-3 are considered inaccurate, while scores from 4-5 are considered accurate.</p>
                    <span class="metric-tag">All out-of-scope questions</span>
                </div>
            </div>
            <h2>Result Interpretation Guide</h2>
            <div class="flex-container">
                <div class="guide-box high-accuracy">
                    <h3>
                        📈 Positive Indicators
                    </h3>
                    <ul>
                        <li>High percentage above 0.9 cosine similarity threshold</li>
                        <li>Majority of responses clustered in 0.85-1.0 range</li>
                        <li>Most relevancy scores at 4-5 range</li>
                        <li>Minimal responses below 0.7 similarity</li>
                    </ul>
                </div>
                <div class="guide-box low-accuracy">
                    <h3>
                        📉 Negative Indicators
                    </h3>
                    <ul>
                        <li>High percentage below 0.9 cosine threshold</li>
                        <li>Large number of 1-3 relevancy scores</li>
                        <li>Wide distribution indicating inconsistency</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
    </html>
    