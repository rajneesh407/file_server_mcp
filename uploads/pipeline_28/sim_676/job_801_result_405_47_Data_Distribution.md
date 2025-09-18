<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Distribution</title>
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
        font-size: 24px;
        font-weight: 600;
        color: #203a58;
        margin-bottom: 4px;
    }
    .header-subtitle {
        font-size: 16px;
        color: #5f6368;
        font-weight: 400;
        margin-bottom: 32px;
    }
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
    }
    .metric-card {
        background: linear-gradient(145deg, #e7f3ff, #ffffff); 
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        border: 1px solid #d1d9e6;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    .card-total-messages {
        border-left: 5px solid #ffc107; /* Amber */
    }
    .card-total-intents {
        border-left: 5px solid #007bff; /* Blue */
    }
    .card-rows-intent {
        border-left: 5px solid #28a745; /* Green */
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
        <span class="metric-number">210</span>
        <div class="metric-label">Total User Messages</div>
    </div>
    <div class="metric-card card-total-intents">
        <div class="metric-icon">🎯</div>
        <span class="metric-number">21</span>
        <div class="metric-label">Total Intents</div>
    </div>
    <div class="metric-card card-rows-intent">
        <div class="metric-icon">📊</div>
        <span class="metric-number">10</span>
        <div class="metric-label">Rows / Intent</div>
    </div>
    </div>
    </div>
    </body>
    </html>
    