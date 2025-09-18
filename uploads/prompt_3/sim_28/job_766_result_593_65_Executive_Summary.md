
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prompt Quality Evaluation</title>
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
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    h3 .pi {
        font-size: 1rem;
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
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        width: 100%;
        margin-top: 1.5rem;
    }
    .card {
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        background-color: #f8f9fa;
    }
    .card ul {
        list-style-type: none;
        padding-left: 0;
        margin-top: 1rem;
    }
    .card li {
        margin-bottom: 0.5rem;
    }
    .guide-box {
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
        <h1>Prompt Quality Evaluation</h1>
        <p class="subtitle">A comprehensive assessment of a prompt's readiness for production using an LLM-as-a-Judge.</p>
        <h2>Methodology</h2>
        <p>This report evaluates the quality and safety of a given prompt by scoring it across six critical dimensions. An advanced LLM-as-a-Judge assesses the prompt for each metric, assigning a score from 1 to 5 and providing a detailed rationale. This dimensional scoring helps quantify the prompt's readiness for deployment.</p>
        <h2>Evaluation Metrics</h2>
        <div class="main-container">
            <div class="card">
                <h3><i class="pi pi-language"></i> Grammatical Correctness</h3>
                <p>Evaluates whether the prompt follows standard grammatical rules, ensuring it is well-written and professional.</p>
                <ul>
                    <li><b>Scale:</b> 1 (Lowest) to 5 (Highest)</li>
                </ul>
            </div>
            <div class="card">
                <h3><i class="pi pi-sun"></i> Clarity</h3>
                <p>Measures how easily the prompt can be understood, based on its organization, language simplicity, and coherence.</p>
                <ul>
                    <li><b>Scale:</b> 1 (Lowest) to 5 (Highest)</li>
                </ul>
            </div>
            <div class="card">
                <h3><i class="pi pi-sitemap"></i> Logical Progression & Coherence</h3>
                <p>Assesses the logical flow and structure of the prompt, ensuring ideas are connected and build on each other effectively.</p>
                <ul>
                    <li><b>Scale:</b> 1 (Lowest) to 5 (Highest)</li>
                </ul>
            </div>
            <div class="card">
                <h3><i class="pi pi-list"></i> Quality of Examples</h3>
                <p>Evaluates the relevance and diversity of any examples provided in the prompt to support the task.</p>
                <ul>
                    <li><b>Scale:</b> 1 (Lowest) to 5 (Highest)</li>
                </ul>
            </div>
            <div class="card">
                <h3><i class="pi pi-shield"></i> Toxicity Safety Score</h3>
                <p>Assesses the likelihood that the prompt could provoke the model to generate toxic or inappropriate responses.</p>
                <ul>
                    <li><b>Scale:</b> 1 (Lowest) to 5 (Highest)</li>
                </ul>
            </div>
            <div class="card">
                <h3><i class="pi pi-eye-slash"></i> Bias Safety Score</h3>
                <p>Evaluates the likelihood that the prompt could lead the model to generate biased or stereotypical responses.</p>
                <ul>
                    <li><b>Scale:</b> 1 (Lowest) to 5 (Highest)</li>
                </ul>
            </div>
        </div>
        <h2>Result Interpretation Guide</h2>
        <div class="main-container">
            <div class="guide-box positive">
                <h3><i class="pi pi-check-circle"></i> Positive Indicators</h3>
                <ul>
                    <li><b>High scores (4-5)</b> across most or all evaluation metrics, indicating a well-constructed and safe prompt.</li>
                    <li>Safety scores (Toxicity & Bias) are <b>5</b>, showing strong guardrails within the prompt.</li>
                    <li>Few or no negative tags identified by the evaluator during the review process.</li>
                </ul>
            </div>
            <div class="guide-box negative">
                <h3><i class="pi pi-exclamation-triangle"></i> Areas for Review</h3>
                <ul>
                    <li><b>Low scores (1-3)</b> in any dimension, especially in Clarity or Logic, which can lead to poor model performance.</li>
                    <li>Safety scores below <b>4</b>, highlighting a critical risk of generating harmful or biased content.</li>
                    <li>Multiple negative tags identified, pointing to specific areas that need improvement.</li>
                </ul>
            </div>
        </div>
    </div>
    </body>
    </html>
    