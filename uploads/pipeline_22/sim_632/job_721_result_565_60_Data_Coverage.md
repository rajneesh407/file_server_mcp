
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coverage Report</title>
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
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
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
    .card-total-messages {
        background: linear-gradient(145deg, #e3f2fd, #ffffff);
        border-left: 5px solid #ffc107; /* Blue */
    }
    .card-num-intents {
        background: linear-gradient(145deg, #e3f2fd, #ffffff);
        border-left: 5px solid #007bff; /* Blue */
    }
    .card-avg-records {
        background: linear-gradient(145deg, #e3f2fd, #ffffff);
        border-left: 5px solid #28a745; /* Blue */
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
    <div class="metric-card card-total-messages">
        <div class="metric-icon">✉️</div>
        <span class="metric-number">1,088</span>
        <div class="metric-label">Total Messages</div>
    </div>
    <div class="metric-card card-num-intents">
        <div class="metric-icon">🎯</div>
        <span class="metric-number">7</span>
        <div class="metric-label">Number of Intents</div>
    </div>
    <div class="metric-card card-avg-records">
        <div class="metric-icon">📊</div>
        <span class="metric-number">155.43</span>
        <div class="metric-label">Avg Records per Intent</div>
    </div>
    </div>
    </div>
    </body>
    </html>
    