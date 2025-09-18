
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #f8f9fa;
        padding: 20px;
        color: #333;
        margin: 0;
    }
    .report-container {
        margin: auto;
    }
    .header {
        font-size: 20px;
        font-weight: 600;
        color: #1c2a4e;
        margin-bottom: 24px;
    }
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 20px;
    }
    .metric-card {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        display: flex;
        flex-direction: column;
    }
    .value-line {
        display: flex;
        align-items: baseline;
        gap: 12px;
        margin-bottom: 8px;
    }
    .main-value {
        font-size: 32px;
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
        color: #3c4043;
        margin: 0;
        flex-grow: 1; 
        padding-bottom: 16px;
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
    <div class="report-container">
        <p>Min/max range across intents is also displayed</p>
        <div class="cards-grid">
            <div class="metric-card" style="background: linear-gradient(145deg, #e7f3ff, #ffffff);">
    <div class="value-line">
        <span class="main-value">0.0%</span>
        <span class="range-tag">Range: (0.0% - 0.0%)</span>
    </div>
    <p class="metric-name">Unnecessary Fact Retrieval Rate (Rule Based)</p>
    <div class="target-line">
        <p class="target-info">Target: < 10%</p>
        <div class="status-icon met">
            ✅
        </div>
    </div>
    </div>
    <div class="metric-card" style="background: linear-gradient(145deg, #e7f3ff, #ffffff);">
    <div class="value-line">
        <span class="main-value">78.0%</span>
        <span class="range-tag">Range: (66.7% - 93.3%)</span>
    </div>
    <p class="metric-name">Answer Relevancy (LLM as a Judge)</p>
    <div class="target-line">
        <p class="target-info">Target: ≥90%</p>
        <div class="status-icon not-met">
            ❌
        </div>
    </div>
    </div>
    
    </div>
    </body>
    </html>
    