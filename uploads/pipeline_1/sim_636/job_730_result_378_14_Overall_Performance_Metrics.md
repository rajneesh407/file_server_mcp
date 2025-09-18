
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            background-color: #f8f9fa;
            padding: 20px;
            color: #333;
        }
        .metrics-container {
            margin: auto;
        }
        .header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 4px;
        }
        .header h2 {
            font-size: 20px;
            font-weight: 600;
            color: #1c2a4e;
            margin: 0;
        }
        .pipeline-icon {
            font-size: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .subtitle {
            font-size: 14px;
            color: #5f6368;
            margin-top: 0;
            margin-bottom: 24px;
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
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
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        .metric-card.metric-overall-accuracy {
            background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        }
        .metric-card.metric-precision {
             background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        }
        .metric-card.metric-recall {
             background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        }
        .metric-card.metric-f1-score {
             background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        }
        .value-line {
            display: flex;
            align-items: baseline;
            gap: 8px;
            margin-bottom: 8px;
        }
        .main-value {
            font-size: 28px;
            font-weight: 600;
            color: #202124;
        }
        .range-tag {
            background-color: #e8eaed;
            color: #5f6368;
            font-size: 12px;
            font-weight: 500;
            padding: 4px 8px;
            border-radius: 12px;
        }
        .metric-name {
            font-size: 16px;       
            font-weight: 600;       
            color: #3c4043;
            margin: 0;
            flex-grow: 1; 
        }
        .target-line {
            margin-top: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .target-info {
            font-size: 14px;
            color: #5f6368;
            margin: 0;
        }
        .status-icon {
            height: 24px;
            width: 24px;
            font-size: 20px; 
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
    </head>
    <body>
        <div class="metrics-container">
            <p class="subtitle" style="color: #34A853;">Meets accuracy expectations of <b>≥90%</b> on diverse test data.</p>
            <div class="cards-grid">
                <div class="metric-card metric-overall-accuracy">
    <div class="value-line">
        <span class="main-value">98.9%</span>
        <span class="range-tag">Range: (95.0% - 100.0%)</span>
    </div>
    <p class="metric-name">Overall Accuracy</p>
    <div class="target-line">
        <p class="target-info">Target: ≥90%</p>
        <div class="status-icon">
            ✅
        </div>
    </div></div><div class="metric-card metric-precision">
    <div class="value-line">
        <span class="main-value">98.9%</span>
        <span class="range-tag">Range: (92.0% - 100.0%)</span>
    </div>
    <p class="metric-name">Precision</p>
    <div class="target-line">
        <p class="target-info">Target: ≥90%</p>
        <div class="status-icon">
            ✅
        </div>
    </div></div><div class="metric-card metric-recall">
    <div class="value-line">
        <span class="main-value">98.9%</span>
        <span class="range-tag">Range: (95.0% - 100.0%)</span>
    </div>
    <p class="metric-name">Recall</p>
    <div class="target-line">
        <p class="target-info">Target: ≥90%</p>
        <div class="status-icon">
            ✅
        </div>
    </div></div><div class="metric-card metric-f1-score">
    <div class="value-line">
        <span class="main-value">98.9%</span>
        <span class="range-tag">Range: (95.8% - 100.0%)</span>
    </div>
    <p class="metric-name">F1 Score</p>
    <div class="target-line">
        <p class="target-info">Target: ≥90%</p>
        <div class="status-icon">
            ✅
        </div>
    </div></div>
            </div>
        </div>
    </body>
    </html>
    