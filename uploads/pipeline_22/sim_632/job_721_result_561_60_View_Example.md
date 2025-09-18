
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example: Perturbed Stability Analysis Calculation</title>
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
        font-size: 0.9rem;
    }
    th, td {
        text-align: left;
        padding: 10px;
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
            <h4>Original User Question</h4>
            <p>"How do I create a new data pipeline in the Corridor Platform?"</p>
        </div>
        <div class="card">
            <h3>Responses from 16 Perturbed Versions</h3>
            <p>The original question is perturbed across 4 dimensions (Length, Urgency, Politeness, Grammar Error), creating 16 unique variations. The LLM-as-a-Judge scores each response.</p>
            <table>
                <thead>
                    <tr>
                        <th>Perturbation (L-U-P-G)</th>
                        <th>Perturbed Question</th>
                        <th>Groundedness Score</th>
                        <th>Answer Relevancy Score</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="lowlight"><td>Short-No-No-Err</td><td>"new pipeline how??"</td><td>Medium</td><td>4</td></tr>
                    <tr class="highlight"><td>Short-No-No-Ok</td><td>"New pipeline how?"</td><td>Very High</td><td>5</td></tr>
                    <tr class="highlight"><td>Short-No-Yes-Err</td><td>"pls new pipeline how??"</td><td>High</td><td>4</td></tr>
                    <tr class="highlight"><td>Short-No-Yes-Ok</td><td>"New pipeline how, please?"</td><td>Very High</td><td>5</td></tr>
                    <tr class="highlight"><td>Short-Yes-No-Err</td><td>"now! new pipeline how??"</td><td>High</td><td>4</td></tr>
                    <tr class="highlight"><td>Short-Yes-No-Ok</td><td>"New pipeline now, how?"</td><td>Very High</td><td>5</td></tr>
                    <tr class="highlight"><td>Short-Yes-Yes-Err</td><td>"pls now new pipeline how??"</td><td>High</td><td>4</td></tr>
                    <tr class="highlight"><td>Short-Yes-Yes-Ok</td><td>"Please, new pipeline now, how?"</td><td>Very High</td><td>5</td></tr>
                    <tr class="lowlight"><td>Long-No-No-Err</td><td>"i want to makes a new data pipeline on corridor, what are steps"</td><td>Medium</td><td>5</td></tr>
                    <tr class="highlight"><td>Long-No-No-Ok</td><td>"I want to make a new data pipeline on Corridor, what are the steps?"</td><td>Very High</td><td>5</td></tr>
                    <tr class="highlight"><td>Long-No-Yes-Err</td><td>"could you pls tell me how to makes a new data pipeline"</td><td>High</td><td>5</td></tr>
                    <tr class="highlight"><td>Long-No-Yes-Ok</td><td>"Could you please tell me how to make a new data pipeline?"</td><td>Very High</td><td>5</td></tr>
                    <tr class="lowlight"><td>Long-Yes-No-Err</td><td>"i need to makes a new data pipeline on corridor right now, what steps"</td><td>Medium</td><td>5</td></tr>
                    <tr class="highlight"><td>Long-Yes-No-Ok</td><td>"I need to make a new data pipeline on Corridor right now, what are the steps?"</td><td>High</td><td>5</td></tr>
                    <tr class="lowlight"><td>Long-Yes-Yes-Err</td><td>"could you pls help me, i need to makes a new data pipeline right now"</td><td>Medium</td><td>5</td></tr>
                    <tr class="highlight"><td>Long-Yes-Yes-Ok</td><td>"Could you please help me? I need to make a new data pipeline right now."</td><td>High</td><td>5</td></tr>
                </tbody>
            </table>
        </div>
        <h2>Metric Computations</h2>
        <div class="main-container">
            <div class="card computation-card">
                <h3>Groundedness Calculation</h3>
                <p><b>Scores:</b> 16 scores with a wide distribution (6x Very High, 6x High, 4x Medium).</p>
                <hr style="border:0; border-top: 1px solid #a3d9b8; margin: 1rem 0;">
                <h4>Total Agreement Rate</h4>
                <p>Compares all 16 scores. Are they identical? No.</p>
                <p class="value">0%</p>
                <h4 style="margin-top: 1rem;">Prediction Stability Rate</h4>
                <p>The most frequent score is "Very High" or "High" (tied at 6 times each).</p>
                <p><b>Calculation:</b> (Number of majority votes) / (Total runs) = 6 / 16</p>
                <p class="value">38%</p>
            </div>
            <div class="card computation-card">
                <h3>Answer Relevancy Calculation</h3>
                <p><b>Scores:</b> 16 scores with a narrow distribution (12x Score 5, 4x Score 4).</p>
                <hr style="border:0; border-top: 1px solid #a3d9b8; margin: 1rem 0;">
                <h4>Total Agreement Rate</h4>
                <p>Compares all 16 scores. Are they identical? No.</p>
                <p class="value">0%</p>
                <h4 style="margin-top: 1rem;">Prediction Stability Rate</h4>
                <p>The most frequent score is "5" (appears 12 times).</p>
                <p><b>Calculation:</b> (Number of majority votes) / (Total runs) = 12 / 16</p>
                <p class="value">75%</p>
            </div>
        </div>
    </div>
    </body>
    </html>
    