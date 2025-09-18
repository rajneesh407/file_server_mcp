
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stability Analysis - Full Screen</title>
    <style>
    body {
        margin: 0;
        padding: 0;
        height: 100%;
    }
    body {
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
    h1, h2, h3 {
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
        gap: 1.5rem;
        margin-top: 1.5rem;
    }
    .flex-container > div {
        flex: 1; 
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
    .guide-box.high-stability {
        border-left-color: #28a745;
    }
    .guide-box.low-stability {
        border-left-color: #dc3545;
    }
    .guide-box h3 {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        font-weight: 600;
    }
    .high-stability h3 { color: #28a745; }
    .low-stability h3 { color: #dc3545; }
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
            <h1>Executive Summary - Stability Analysis</h1>
            <p class="subtitle">Assessment of model consistency and reliability across repeated testing scenarios</p>
            <h2>Testing Methodology</h2>
            <p>Stability testing involves running identical inputs through the model multiple times (X=5 repetitions) to measure consistency of responses and identify potential variability issues.</p>
            <div class="flex-container">
                <div class="info-box">
                    <h3>Total Agreement Rate</h3>
                    <p>Percentage of cases where all X repetitions produced identical responses (regardless of correctness)</p>
                </div>
                <div class="info-box">
                    <h3>Stability Percentage</h3>
                    <p>The percentage of repeated model responses that agree with the majority output for each test case. For each input tested five times, this metric calculates how often the model's outputs match the most common response among those repetitions, reflecting the consistency of the model’s behavior.</p>
                </div>
            </div>
            <h2>Result Interpretation Guide</h2>
            <div class="flex-container">
                <div class="guide-box high-stability">
                    <h3>
                        ✅ Signs of High Stability
                    </h3>
                    <ul>
                        <li>High total agreement rates across intents</li>
                        <li>Strong stability percentages consistently</li>
                        <li>Consistent performance across all intent categories</li>
                        <li>Low variance in repeated testing results</li>
                    </ul>
                </div>
                <div class="guide-box low-stability">
                    <h3>
                        ❌ Signs of Low/Weak Stability
                    </h3>
                    <ul>
                        <li>Low total agreement rates for any intent</li>
                        <li>Poor stability percentages across categories</li>
                        <li>High variability between repetitions</li>
                        <li>Inconsistent responses for identical inputs</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
    </html>
    