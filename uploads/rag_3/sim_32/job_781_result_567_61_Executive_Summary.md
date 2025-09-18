
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary: Credit Card Info Retrieval Accuracy</title>
    <style>
    details.collapsible.page {
        border: 1px solid #e9ecef;
        border-radius: 8px;
        background-color: #ffffff;
        margin: 1rem;
    }
    details.collapsible.page summary {
        list-style: none;               /* hide default marker */
        display: flex;
        align-items: center;
        justify-content: space-between; /* title left, chevron right */
        gap: 0.75rem;
        padding: 0.75rem 1rem;
        cursor: pointer;
        user-select: none;
    }
    details.collapsible.page summary::-webkit-details-marker { display: none; }
    details.collapsible.page .h1-like {
        font-size: 2rem;  /* match your h1 size */
        font-weight: 600;
        color: #212529;
        margin: 0;
    }
    details.collapsible.page .chev::before {
        content: "▸";
        color: #6c757d;
        font-size: 1.1rem;
    }
    details.collapsible.page[open] .chev::before {
        content: "▾";
    }
    details.collapsible.page .collapsible-body {
        padding: 0; /* keep your existing .content-wrapper padding intact */
    }
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
        align-items: stretch;
    }
    .card {
        flex: 1;
        min-width: 300px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        background-color: #f8f9fa;
        display: flex;
        flex-direction: column;
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
        content: '✔';
        position: absolute;
        left: 0;
        color: currentColor;
    }
    .guide-box.negative li::before {
        content: '✘';
    }
    .metrics-list {
        margin-top: 0.75rem;
        padding-left: 1.25rem; /* indent bullets */
        list-style: disc;
    }
    .metrics-list li::marker {
        font-size: 1.1em; /* slightly larger marker (optional) */
    }
    .metrics-list li:nth-child(1)::marker {
        color: #fd7e14; /* orange */
    }
    .metrics-list li:nth-child(2)::marker {
        color: #0d6efd; /* blue */
    }
    #key-metrics .card h3 {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem; /* space between dot and text */
    }
    #key-metrics .card h3::before {
        content: "";
        width: 0.6em;
        height: 0.6em;
        border-radius: 50%;
        display: inline-block;
        flex: 0 0 auto;
        /* default color as fallback (optional) */
        background-color: #adb5bd;
    }
    #key-metrics .card:nth-of-type(1) h3::before {
        background-color: #fd7e14; /* orange */
    }
    #key-metrics .card:nth-of-type(2) h3::before {
        background-color: #0d6efd; /* blue */
    }
    .pill {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        line-height: 1.2;
        white-space: nowrap; /* keeps pill on one line if possible */
        border: 1px solid transparent;
    }
    .pill.orange {
        color: #fd7e14;
        background-color: #fff3e6; /* light orange */
        border-color: rgba(253, 126, 20, 0.35);
    }
    .pill.blue {
        color: #0d6efd;
        background-color: #e7f1ff; /* light blue */
        border-color: rgba(13, 110, 253, 0.35);
    }
    .metric-note {
        margin-top: 1rem;
    }
    .card .metric-note {
        margin-top: auto;
        padding-top: 1rem;
    }
    </style>
    </head>
    <body>
    <details class="collapsible page" open>
        <summary>
            <span class="h1-like">Executive Summary - Credit Card Info Retrieval Accuracy</span>
            <span class="chev"></span>
        </summary>
        <div class="collapsible-body">
        <div class="content-wrapper">
            <p class="subtitle">Accuracy measurement of the credit card information retrieval system focuses on (i) whether it avoids executing a database (DB) call when it is not required and (ii) whether the returned data aligns with ground truth when a database call is expected. Ground Truth is provided as a SQL query that is executed on the knowledgebase, ensuring the evaluation is compatible with dynamic knowledgebases.</p>
            <h2>Testing Methodology</h2>
            <p>Input-output testing is performed with user messages that are known to either require a database call to retrieve the customer's card information or not require a database call, resulting in two metrics:</p>
            <ul class="metrics-list">
                <li>If the user message <i>does not require database call</i>, does the system correctly avoid making database call?</li>
                <li>If the user message <i>requires a database call</i>, how well does the system retrieved card information match the data retrieved by the ground truth SQL query?</li>
            </ul>
            <h2>Key Metrics</h2>
            <div class="main-container" id="key-metrics">
                <div class="card">
                    <h3>System accurately avoids a database call.</h3>
                    <p>Outcomes are:</p>
                    <ul>
                        <li><b>True</b> - system did not attempt a database call</li>
                        <li><b>False</b> - system attempated a database call</li>
                    </ul>
                    <p class="metric-note">
                        <span class="pill orange">Only questions where no database call is required</span>
                    </p>
                </div>
                <div class="card">
                    <h3>System retrieved details from the correct cards.</h3>
                    <p>Outcomes are bucketed based on comparison with ground truth SQL queries: 
                    <ul>
                        <li><b>Exact match</b></li>
                        <li><b><b>Contains correct cards</b> (superset of ground truth)</b></li>
                        <li><b>Incorrect match</b></p></li>
                        <li><b>No database call</b> (system skipped required call)</li>
                    </ul>
                    <p class="metric-note"> 
                        <span class="pill blue">Only questions where a database call is required</span>
                    </p>
                </div>
            </div>
            <h2>Result Interpretation Guide</h2>
            <div class="main-container">
                <div class="guide-box positive">
                    <h3><i class="pi pi-check-circle"></i> Positive Indicators</h3>
                    <ul>
                        <li>High proportion of <b>Accurate avoidance of database call</b> (the system consistently avoids unnecessary DB calls).</li>
                        <li>High proportion of <b>Exact match</b> (returned cards precisely match ground truth).</li>
                        <li>Consistent performance across intent categories (narrow spread when sliced by intent).</li>
                    </ul>
                </div>
                <div class="guide-box negative">
                    <h3><i class="pi pi-exclamation-triangle"></i> Negative Indicators</h3>
                    <ul>
                        <li>High proportion of <b>No database call</b> when data is expected (the system fails to retrieve when it should).</li>
                        <li>High proportion <b>Incorrect match</b> (missing required cards or returning wrong cards), signaling SQL generation or retrieval issues.</li>
                    </ul>
                        Note: While <b>Contains correct cards</b> or <b>unnecessary database call</b> signal weakness in the Retrieval system, it does not necessarily have a detrimental impact on the Conversational AI Chatbot pipeline overall, as the Response Model may still be able to generate the right response to the customer.
                </div>
            </div>
        </div>
    </details>
    </body>
    </html>
    