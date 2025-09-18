
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Executive Summary: Corridor Bot Accuracy Testing</title>
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
                gap: 2.5rem; /* Adjusted gap to match original snippet */
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
            /* Styles for interpretation guide from the first code snippet */
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
        <h1>Response Accuracy Assessment</h1>
        <p class="subtitle">LLM-as-a-Judge evaluation for Answer Relevancy and Groundedness.</p>
        <h2>Methodology</h2>
        <p>The Corridor Bot's accuracy is evaluated using a broad set of user queries. Each response is systematically assessed by an LLM-as-a-Judge model, which provides scores for two distinct dimensions: how relevant the answer is to the user's question and how well-grounded it is on the website contents fetched by the agent. This dual-metric approach ensures a holistic view of the bot's performance, verifying both its helpfulness and its factual integrity.</p>
        <h2>Metrics</h2>
        <div class="main-container">
            <div class="card">
                <h3><i class="pi pi-check"></i> Answer Relevancy</h3>
                <p>This metric assesses how well the bot's response aligns with the user's query. It focuses on whether the answer directly addresses the question, stays on topic, and provides the information sought by the user in a helpful manner.</p>
                <ul style="margin-top: 8px;">
                    <li><b>Scale:</b> 1 to 5 (5 being the most relevant), and "Cannot Determine".</li>
                    <li><b>Success Threshold:</b> Scores of 4 or 5 are considered helpful and relevant.</li>
                </ul>
            </div>
            <div class="card">
                <h3><i class="pi pi-link"></i> Groundedness</h3>
                <p>This metric evaluates the factual accuracy of the bot's response by checking if the information provided is fully supported by the underlying source material. It is crucial for preventing hallucinations and ensuring the bot is a reliable source of information.</p>
                <ul style="margin-top: 8px;">
                    <li><b>Scale:</b> Very High, High, Medium, Low, Very Low, Cannot Determine</li>
                    <li><b>Success Threshold:</b> Ratings of "High" or "Very High" are considered correctly grounded.</li>
                </ul>
            </div>
        </div>
        <h2>Result Interpretation Guide</h2>
        <div class="main-container">
            <div class="guide-box positive">
                <h3><i class="pi pi-check-circle"></i> Positive Indicators</h3>
                <ul>
                    <li>A high percentage of responses scoring 4 or 5 for Answer Relevancy.</li>
                    <li>A high percentage of responses rated as "High" or "Very High" for Groundedness.</li>
                    <li>Stable and reliable performance across a diverse range of topics.</li>
                </ul>
            </div>
            <div class="guide-box negative">
                <h3><i class="pi pi-exclamation-triangle"></i> Areas for Review</h3>
                <ul>
                    <li>A significant number of responses with low Answer Relevancy scores (1-3).</li>
                    <li>Frequent "Low" or "Very Low" Groundedness ratings, indicating hallucinations.</li>
                    <li>Inconsistent performance on specific types of questions or topics.</li>
                </ul>
                <p style="margin-top: 1rem;"><b>Note: </b>"Cannot Determine" scores represent questions that the bot was unable to answer based on content it was given. It may be due to information not being available, or failure of the bot to retrieve existing relevant information. Hence, these warrant further investigation.</p>
            </div>
        </div>
    </div>
    </body>
    </html>
    