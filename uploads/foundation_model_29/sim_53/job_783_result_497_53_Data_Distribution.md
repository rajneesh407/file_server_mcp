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
    .metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); 
    gap: 20px;
    }
    .metric-card {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    background: linear-gradient(145deg, #e7f3ff, #ffffff);
    }
    .metric-label {
        font-size: 16px;
        color: #5f6368;
        font-weight: 500;
    }
    .metric-number {
        font-size: 36px;
        font-weight: 700;
        color: #202124;
        display: block;
        margin-bottom: 4px;
        line-height: 1.2;
    }
    </style>
    </head>
    <body>
    <div class="dashboard-container">
    <div class="metrics-grid">
    <div class="metric-card">
        <div class="metric-label">Total Rows</div>
        <span class="metric-number">10</span>
    </div>
    <div class="metric-card">
        <div class="metric-label">Unique Intents</div>
        <span class="metric-number">7</span>
    </div>
    <div class="metric-card">
        <div class="metric-label">Avg Rows/Intent</div>
        <span class="metric-number">1.4</span>
    </div>
    <div class="metric-card">
        <div class="metric-label">Score Coverage</div>
        <span class="metric-number">1-5</span>
    </div>
    </div>
    </div>
    </body>
    </html>
    