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
    .header-title {
        font-size: 22px;
        font-weight: 600;
        color: #1c2a4e;
        margin-bottom: 8px;
    }
    .header-subtitle {
        font-size: 16px;
        color: #5f6368;
        font-weight: 400;
        margin-bottom: 32px;
    }
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
        gap: 20px;
    }
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    .card-samples {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 4px solid #42a5f5;
    }
    .card-intents {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 4px solid #66bb6a;
    }
    .card-average {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 4px solid #ab47bc;
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
    <div class="metrics-grid">
    <div class="metric-card card-samples">
        <div class="metric-icon">📋</div>
        <span class="metric-number">976</span>
        <div class="metric-label">Total Samples</div>
    </div>
    <div class="metric-card card-intents">
        <div class="metric-icon">🏷️</div>
        <span class="metric-number">7</span>
        <div class="metric-label">Total Intents</div>
    </div>
    <div class="metric-card card-average">
        <div class="metric-icon">➗</div>
        <span class="metric-number">139.4</span>
        <div class="metric-label">Average Samples / Intent</div>
    </div>
    </div>
    </div>
    </body>
    </html>
    