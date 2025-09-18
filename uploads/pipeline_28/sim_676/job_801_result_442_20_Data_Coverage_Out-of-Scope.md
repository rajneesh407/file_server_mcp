
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 24px;
        }
        .metrics-container h2 {
            font-size: 20px;
            font-weight: 600;
            color: #1c2a4e;
            margin-top: 0;
            margin-bottom: 20px;
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }
        .metric-card {
            border: 1px solid #cde4fe;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            text-align: center;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            background: linear-gradient(145deg, #e7f3ff, #f8faff);
        }
        .metric-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        .value-line {
            margin-bottom: 8px;
        }
        .main-value {
            font-size: 36px;
            font-weight: 600;
            color: #0d6efd;
        }
        .metric-name {
            font-size: 15px;
            font-weight: 500;
            color: #5f6368;
            margin: 0;
        }
        @media (max-width: 768px) {
            .cards-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    </head>
    <body>
    <div class="metrics-container">
        <h2>Out-of-Scope Testing Coverage</h2>
        <div class="cards-grid">
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">672</span>
        </div>
        <p class="metric-name">Total Messages</p>
    </div>
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">21</span>
        </div>
        <p class="metric-name">Number of Intents</p>
    </div>
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">32</span>
        </div>
        <p class="metric-name">Avg Records per Intent</p>
    </div>
        </div>
    </div>
    </body>
    </html>
    