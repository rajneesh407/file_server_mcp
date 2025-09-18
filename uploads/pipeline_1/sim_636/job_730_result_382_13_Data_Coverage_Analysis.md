<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        background-color: #f8f9fa;
        color: #333;
        margin: 0;
        padding: 20px;
        box-sizing: border-box;
    }
    .dashboard-container {
        max-width: 100%;
        margin: auto;
    }
    .header-subtitle {
        font-size: 16px;
        color: #5f6368;
        font-weight: 400;
        margin-bottom: 32px;
    }
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
        gap: 20px;
    }
    .metric-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        border: 1px solid #e0e0e0;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    .card-total-utterances {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #ffc107;
    }
    .card-unique-utterances {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #007bff;
    }
    .card-repetitions {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #28a745;
    }
    .card-intents {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #6f42c1;
    }
    .metric-icon {
        font-size: 32px;
        margin-bottom: 16px;
        line-height: 1;
    }
    .metric-number {
        font-size: 44px;
        font-weight: 700;
        color: #203a58;
        display: block;
        margin-bottom: 4px;
        line-height: 1.1;
    }
    .metric-label {
        font-size: 15px;
        color: #4a6a8a;
        font-weight: 500;
    }
    </style>
    </head>
    <body>
    <div class="dashboard-container">
    <p class="header-subtitle">Overview of test data distribution and repetition patterns</p>
    <br>
    <div class="metrics-grid">
    <div class="metric-card card-total-utterances">
        <div class="metric-icon">📝</div>
        <span class="metric-number">3,900</span>
        <div class="metric-label">Total Utterances</div>
    </div>
    <div class="metric-card card-unique-utterances">
        <div class="metric-icon">💬</div>
        <span class="metric-number">780</span>
        <div class="metric-label">Unique Utterances</div>
    </div>
    <div class="metric-card card-repetitions">
        <div class="metric-icon">🔁</div>
        <span class="metric-number">5</span>
        <div class="metric-label">Average Repetitions</div>
    </div>
    <div class="metric-card card-intents">
        <div class="metric-icon">🗂️</div>
        <span class="metric-number">26</span>
        <div class="metric-label">Intents Covered</div>
    </div>
    </div>
    </div>
    </body>
    </html>
    