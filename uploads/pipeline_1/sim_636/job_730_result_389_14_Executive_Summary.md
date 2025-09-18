<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accuracy Analysis - Full Screen</title>
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
    <h1>Executive Summary - Accuracy Analysis</h1>
    <p class="subtitle">Comprehensive assessment of intent classification accuracy across various intent categories</p>
    <h2>Testing Methodology</h2>
    <p>An input-output testing approach compares the model's predicted intent for each user message against the ground truth label. Metrics are calculated groupping them by intent class to capture detailed performance across diverse customer utterances and scenarios.</p>
    <div class="flex-container">
        <div class="info-box">
            <h3>Accuracy</h3>
            <p>Correct predictions / Total predictions</p>
        </div>
        <div class="info-box">
            <h3>Precision</h3>
            <p>True positives / (True positives + False positives)</p>
        </div>
        <div class="info-box">
            <h3>Recall</h3>
            <p>True positives / (True positives + False negatives)</p>
        </div>
        <div class="info-box">
            <h3>F1 Score</h3>
            <p>Harmonic mean of precision and recall</p>
        </div>
    </div>
    <p style="margin-top: 1rem;">The overall precision, recall, and F1 score reported are averages aggregated across all intent classes, providing a holistic view of classification effectiveness.</p>
    <h2>Result Interpretation Guide</h2>
    <div class="flex-container">
        <div class="guide-box high-accuracy">
            <h3>
                ✅ Signs of High Accuracy
            </h3>
            <ul>
                <li>Consistently high accuracy scores across most intents</li>
                <li>F1 scores showing strong performance</li>
                <li>Low variance between precision and recall</li>
                <li>Balanced performance across all intent categories</li>
            </ul>
        </div>
        <div class="guide-box low-accuracy">
            <h3>
                ❌ Signs of Low/Weak Accuracy
            </h3>
            <ul>
                <li>Low accuracy scores for any intent category</li>
                <li>Large gaps between precision and recall metrics</li>
                <li>Significant performance variance across intents</li>
                <li>High misclassification rates for critical intents</li>
            </ul>
        </div>
    </div>
    </div>
    </body>
    </html>
    