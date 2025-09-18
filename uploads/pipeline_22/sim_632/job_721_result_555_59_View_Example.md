
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example: Stability Analysis Calculation</title>
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
        font-size: 1.25rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid #e9ecef;
        padding-bottom: 0.5rem;
    }
    h4 {
        font-size: 1.1rem;
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
    .response-card {
        background-color: #fff;
        border-left: 4px solid #007bff;
    }
    .computation-card {
        background-color: #e9f7ef;
        border-color: #a3d9b8;
    }
    .computation-card .value {
        font-weight: bold;
        font-size: 1.2rem;
        color: #1d6a43;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 1rem;
    }
    th, td {
        text-align: left;
        padding: 12px;
        border-bottom: 1px solid #e9ecef;
    }
    th {
        background-color: #f8f9fa;
    }
    .highlight {
        background-color: #d4edda; /* Light green for Very High/High scores */
    }
    .lowlight {
        background-color: #f8d7da; /* Light red for Low scores */
    }
    </style>
    </head>
    <body>
    <div class="content-wrapper">
        <div class="card response-card">
            <h4>User Question</h4>
            <p>"How do I create a new data pipeline in the Corridor Platform?"</p>
        </div>
        <div class="card">
            <h3>Responses from 5 Repeated Runs</h3>
            <p>The same question is sent through the pipeline 5 times, and the LLM-as-a-Judge scores each response.</p>
            <table>
                <thead>
                    <tr>
                        <th>Run #</th>
                        <th>LLM Response</th>
                        <th>Groundedness Score</th>
                        <th>Answer Relevancy Score</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="highlight">
                        <td>1</td>
                        <td>"Navigate to the 'Pipelines' tab and click 'New Pipeline' to start the wizard."</td>
                        <td>Very High</td>
                        <td>5</td>
                    </tr>
                    <tr class="highlight">
                        <td>2</td>
                        <td>"You can create a new pipeline by going to the 'Pipelines' section and selecting 'Create New'."</td>
                        <td>Very High</td>
                        <td>5</td>
                    </tr>
                    <tr class="lowlight">
                        <td>3</td>
                        <td>"To create a pipeline, go to the 'Projects' tab first, then find the pipeline creator."</td>
                        <td>Low</td>
                        <td>3</td>
                    </tr>
                    <tr class="highlight">
                        <td>4</td>
                        <td>"Just click the 'New Pipeline' button in the 'Pipelines' area to begin."</td>
                        <td>Very High</td>
                        <td>5</td>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td>"Creating a new pipeline is done in the 'Pipelines' tab. Click 'New'."</td>
                        <td>High</td>
                        <td>4</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <h2>Metric Computations</h2>
        <div class="main-container">
            <div class="card computation-card">
                <h3>Groundedness Calculation</h3>
                <p><b>Scores:</b> [Very High, Very High, Low, Very High, High]</p>
                <hr style="border:0; border-top: 1px solid #a3d9b8; margin: 1rem 0;">
                <h4>Total Agreement Rate</h4>
                <p>Compares all 5 scores. Are they identical? In this case, no.</p>
                <p class="value">0%</p>
                <h4 style="margin-top: 1rem;">Prediction Stability Rate</h4>
                <p>Find the most frequent score (the majority vote). "Very High" appears 3 times.</p>
                <p><b>Calculation:</b> (Number of majority votes) / (Total runs) = 3 / 5</p>
                <p class="value">60%</p>
            </div>
            <div class="card computation-card">
                <h3>Answer Relevancy Calculation</h3>
                <p><b>Scores:</b> [5, 5, 3, 5, 4]</p>
                <hr style="border:0; border-top: 1px solid #a3d9b8; margin: 1rem 0;">
                <h4>Total Agreement Rate</h4>
                <p>Compares all 5 scores. Are they identical? No.</p>
                <p class="value">0%</p>
                <h4 style="margin-top: 1rem;">Prediction Stability Rate</h4>
                <p>Find the most frequent score. Score "5" appears 3 times.</p>
                <p><b>Calculation:</b> (Number of majority votes) / (Total runs) = 3 / 5</p>
                <p class="value">60%</p>
            </div>
        </div>
    </div>
    </body>
    </html>
    