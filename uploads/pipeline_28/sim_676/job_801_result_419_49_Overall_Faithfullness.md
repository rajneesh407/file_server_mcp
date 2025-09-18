
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            height: 100%; margin: 0; padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            background-color: #f8f9fa; color: #333;
        }
        .metrics-container {
            width: 100%; height: 100%; padding: 24px; box-sizing: border-box;
            display: flex; flex-direction: column;
        }
        .metrics-container h2 {
            font-size: 24px; font-weight: 600; color: #1c2a4e;
            margin-top: 0; margin-bottom: 24px; flex-shrink: 0;
        }
        .cards-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 24px; flex-grow: 1;
        }
        .metric-card {
            background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px;
            padding: 24px; box-shadow: 0 2px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            background: linear-gradient(145deg, #e7f3ff, #ffffff);
        }
        .metric-card:hover { transform: translateY(-4px); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
        .value-line { display: flex; align-items: baseline; gap: 8px; margin-bottom: 8px; }
        .main-value { font-size: 32px; font-weight: 600; color: #202124; }
        .range-tag {
            background-color: #e8eaed; color: #5f6368; font-size: 12px;
            font-weight: 500; padding: 4px 8px; border-radius: 12px;
        }
        .metric-name { font-size: 16px; font-weight: 600; color: #3c4043; margin: 0; flex-grow: 1; }
        .target-line { margin-top: 16px; display: flex; justify-content: space-between; align-items: center; }
        .target-info { font-size: 14px; color: #5f6368; margin: 0; }
        .status-icon { font-size: 20px; }
    </style>
    </head>
    <body>
    <div class="metrics-container">
        <div class="cards-grid">
            
    <div class="metric-card">
    <div class="value-line">
        <span class="main-value">98.9%</span>
        <span class="range-tag">Range: (94.4% - 100.0%)</span>
    </div>
    <p class="metric-name">Average Faithfulness</p>
    <div class="target-line">
        <p class="target-info">Target: ≥90.0%</p>
        <div class="status-icon">
            ✅
        </div>
    </div>
    </div>
    
    </div>
    </body>
    </html>
        