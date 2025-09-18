
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary: Financial Terms Understanding</title>
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
    .card ul {
        list-style-type: none;
        padding-left: 0;
        margin-top: 0.75rem;
    }
    .card ul li {
        position: relative;
        padding-left: 1.25em;
        margin-bottom: 0.5rem;
    }
    .card ul li::before {
        content: '•';
        position: absolute;
        left: 0;
        color: #6c757d;
        font-size: 1.25em;
        line-height: 1;
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
        <h1>Financial Terms Understanding</h1>
        <p class="subtitle">An evaluation of large language models on their ability to accurately define financial vocabulary.</p>
        <h2>Methodology</h2>
        <p>This report assesses the capability of various foundation models to understand and define financial terms. Each model is prompted to generate a definition for a given financial term. The generated definition is then compared against the actual, ground-truth definition using two distinct evaluation methods: a machine learning-based similarity score and an LLM-as-a-Judge assessment.</p>
        <h2>Metrics</h2>
        <div class="main-container">
            <div class="card">
                <h3><i class="pi pi-calculator"></i> Cosine Similarity</h3>
                <p>This metric measures the contextual similarity between the model's generated definition and the actual definition. It works by converting both texts into numerical vectors (embeddings) and calculating the cosine of the angle between them. A higher score (closer to 100) indicates a greater semantic similarity.</p>
            </div>
            <div class="card">
                <h3><i class="pi pi-user"></i> LLM Similarity</h3>
                <p>This metric uses a separate, powerful language model (an 'LLM-as-a-Judge') to assess the quality of the generated definition. The judge compares the generated and actual definitions and assigns a score based on how well they align in meaning and context.</p>
                 <ul style="margin-top: 8px;">
                    <li><b>Scale:</b> 1 (Not Related) to 5 (Nearly Identical).</li>
                    <li><b>Success Threshold:</b> Scores of 4 or 5 are considered high-quality definitions.</li>
                </ul>
            </div>
        </div>
        <h2>Result Interpretation Guide</h2>
        <div class="main-container">
            <div class="guide-box positive">
                <h3><i class="pi pi-check-circle"></i> Positive Indicators</h3>
                <ul>
                    <li><b>High average scores</b> for both Cosine and LLM Similarity, indicating strong overall performance.</li>
                    <li>A high percentage of responses scoring <b>4 or 5 for LLM Similarity</b>, showing the model consistently generates accurate definitions.</li>
                    <li><b>Consistent performance</b> across different categories (visible in the radar chart), suggesting a broad and reliable understanding of financial topics.</li>
                </ul>
            </div>
            <div class="guide-box negative">
                <h3><i class="pi pi-exclamation-triangle"></i> Areas for Review</h3>
                <ul>
                    <li><b>Low average scores</b>, pointing to a general weakness in the model's financial knowledge.</li>
                    <li>A significant number of responses with <b>low LLM Similarity scores (1-3)</b>, indicating frequent irrelevant or incorrect definitions.</li>
                    <li><b>Poor performance on specific categories</b>, highlighting potential knowledge gaps that may require targeted fine-tuning.</li>
                </ul>
            </div>
        </div>
    </div>
    </body>
    </html>
    