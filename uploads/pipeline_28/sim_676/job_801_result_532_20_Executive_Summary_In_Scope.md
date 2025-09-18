
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Executive Summary: Stability Analysis</title>
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
                margin-bottom: 1.5rem;
            }
            h3 {
                font-size: 1.15rem;
                margin-bottom: 0.75rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            p {
                line-height: 1.6;
                margin: 0;
                margin-bottom: 2rem;
            }
            .flex-container {
                display: flex;
                flex-wrap: wrap;
                gap: 1.5rem;
            }
            .flex-container > div {
                flex: 1;
                min-width: 300px;
            }
            .info-box {
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 8px;
                padding: 1.5rem;
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
                font-size: 1.25em;
                line-height: 1;
            }
            .high-accuracy li::before { color: #28a745; }
            .low-accuracy li::before { color: #dc3545; }
            .stability-measurements ul {
                list-style-type: none;
                padding-left: 0;
                margin: 0;
            }
            .stability-measurements li {
                margin-bottom: 1rem;
            }
            .stability-measurements li:last-child {
                margin-bottom: 0;
            }
            .stability-measurements strong {
                display: block;
                margin-bottom: 0.25rem;
            }
            .metric-type-tag {
                font-size: 0.8rem;
                font-weight: 500;
                padding: 0.2rem 0.6rem;
                border-radius: 12px;
                color: #fff;
                margin-left: 0.5rem;
            }
            .core-metric {
                background-color: #007bff;
            }
            .llm-judge {
                background-color: #6f42c1;
            }
            .guide-box h3 small {
                font-weight: 500;
                font-size: 0.9rem;
                color: #5a626a;
            }
        </style>
    </head>
    <body>
        <div class="content-wrapper">
        <h1>Credit Card Intents Executive Summary</h1>
            <h2>Testing Methodology</h2>
            <p>Input-output testing of perturbed user messages across multiple dimensions (length, grammar, politeness, synonyms, formality, spelling variations) through the pipeline. Evaluate the stability of the output of the generated response. Stability is measured as total agreement rate and percentage of stable records of the 2 accuracy metrics (factual accuracy and answer relevancy).</p>
            <h2>Stability Measurements</h2>
            <div class="flex-container">
                <div class="info-box stability-measurements">
                    <h3><span>Factual Accuracy</span> <span class="metric-type-tag core-metric">Core Metric</span></h3>
                    <ul>
                        <li><strong>Definition:</strong><br>Evaluates whether the facts (credit card details) referenced by the model match the ground truth facts. Categories include Fully Correct, Partially Correct, Not Correct, and No Fact Retrieved.</li>
                        <li><strong>Total Agreement Rate:</strong><br>% of user messages with identical factual accuracy outcome across all perturbed dimensions</li>
                        <li><strong>Percentage of Stable Records:</strong><br>% of stable results among perturbed dimensions</li>
                    </ul>
                </div>
                <div class="info-box stability-measurements">
                    <h3><span>Answer Relevancy</span> <span class="metric-type-tag llm-judge">LLM Judge</span></h3>
                    <ul>
                        <li><strong>Definition:</strong><br>LLM-as-a-judge scoring on a 1-5 scale measuring how well the response addresses the user query. Scores 4-5 are considered accurate/relevant.</li>
                        <li><strong>Total Agreement Rate:</strong><br>% of user messages with identical answer relevancy scores across all perturbed dimensions</li>
                        <li><strong>Percentage of Stable Records:</strong><br>% of stable results among perturbed dimensions</li>
                    </ul>
                </div>
            </div>
            <h2>Result Interpretation Guide</h2>
            <div class="flex-container">
                <div class="guide-box high-accuracy">
                    <h3>
                        ✅ Positive Indicators
                    </h3>
                    <ul>
                        <li>High agreement rates (>80%) with consistent factual accuracy across all perturbations</li>
                        <li>Minimal variation between original and perturbed message responses</li>
                    </ul>
                </div>
                <div class="guide-box low-accuracy">
                    <h3>
                        ⚠️ Areas for Review
                    </h3>
                    <ul>
                        <li>Low agreement rates (<60%) indicating instability requiring prompt engineering to improve response quality.</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
    </html>
    