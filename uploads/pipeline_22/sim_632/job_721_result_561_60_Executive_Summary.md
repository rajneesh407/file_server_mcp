
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary: Perturbed Stability Analysis</title>
    <link rel="stylesheet" href="https://unpkg.com/primeicons/primeicons.css">
    <style>
    body {
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        background-color: #ffffff;
        color: #5a626a;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    .content-wrapper {
        width: 100%;
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
    p, li {
        line-height: 1.6;
        margin: 0;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }
    .main-container {
        display: flex;
        flex-wrap: wrap; 
        gap: 2.5rem;
        width: 100%;
        margin-top: 1.5rem;
    }
    .card {
        flex: 1;
        min-width: 300px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        background-color: #f8f9fa;
    }
    .guide-box {
        flex: 1;
        min-width: 300px;
        border-radius: 6px;
        padding: 1.5rem;
    }
    .guide-box.positive {
        background-color: #e9f7ef;
        border: 1px solid #a3d9b8;
        color: #1d6a43;
    }
    .guide-box.negative {
        background-color: #fbe9e9;
        border: 1px solid #f2b5b5;
        color: #8b2c2c;
    }
    .guide-box ul {
        list-style-type: none;
        padding-left: 0;
        margin-top: 0.75rem;
    }
    .guide-box li {
        position: relative;
        padding-left: 1.25em;
        margin-bottom: 0.5rem;
    }
    .guide-box li::before {
        content: '•';
        position: absolute;
        left: 0;
        color: currentColor;
        font-size: 1.25em;
        line-height: 1;
    }
    </style>
    </head>
    <body>
    <div class="content-wrapper">
        <h1>Perturbed Stability Analysis</h1>
        <h2>Methodology</h2>
        <p>This analysis tests in-scope intents by perturbing each user question across multiple dimensions (e.g., length, politeness, grammar). The pipeline evaluates the stability of the generated responses. Each response is scored by an LLM-as-a-Judge for Groundedness and Answer Relevancy to measure how well accuracy holds up against variations in user input.</p>
        <h2>Metrics</h2>
        <div class="main-container">
            <div class="card">
                <h3>Groundedness</h3>
                <p>Measures if the facts in the response are correct according to the retrieved data chunks. Assessed by an LLM-as-a-Judge.</p>
                <p style="margin-top: 1rem;"><b>Total Agreement Rate:</b> % of user messages with identical groundedness scores across all perturbed variations.</p>
                <p style="margin-top: 0.5rem;"><b>Prediction Stability Rate:</b> The percentage of perturbed responses that match the most frequent (majority vote) score.</p>
            </div>
            <div class="card">
                <h3>Answer Relevancy</h3>
                <p>Measures if the generated answer is relevant to the user's question. Assessed by an LLM-as-a-Judge.</p>
                <p style="margin-top: 1rem;"><b>Total Agreement Rate:</b> % of user messages with all identical answer relevancy scores across all perturbed variations.</p>
                <p style="margin-top: 0.5rem;"><b>Prediction Stability Rate:</b> The percentage of perturbed responses that match the most frequent (majority vote) score.</p>
            </div>
        </div>
        <h2>Result Interpretation Guide</h2>
        <div class="main-container">
            <div class="guide-box positive">
                <h3><i class="pi pi-check-circle"></i> Positive Indicators</h3>
                <ul>
                    <li><b>High agreement rates:</b> The model consistently produces the same score for both Groundedness and Relevancy across all repeated runs.</li>
                    <li><b>High stability rates:</b> Indicates that most repeated runs generate the same Groundedness and Relevancy. This score can be high despite low agreement rate if e.g. 4 out of 5 responses are stable.</li>
                </ul>
            </div>
            <div class="guide-box negative">
                <h3><i class="pi pi-exclamation-triangle"></i> Areas for Review</h3>
                <ul>
                    <li><b>Low stability rates:</b> The bot's response is vulnerable to changes in phrasing, indicating a lack of robustness.</li>
                    <li><b>Potential for unreliable answers:</b> If stability is low, scrutinize the response to determine if the bot is generating irrelevant or factually incorrect information, or if it is the LLM-as-a-judge showing minor variability in its scores.</li>
                </ul>
            </div>
        </div>
    </div>
    </body>
    </html>
    