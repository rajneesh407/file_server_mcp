
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <style>
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        background-color: #f8f9fa;
        padding: 20px;
        color: #333;
      }
      .metrics-container {
        margin: auto;
        max-width: 100%;
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
      .subtitle {
        font-size: 14px;
        color: #5f6368;
        margin-top: 0;
        margin-bottom: 24px;
      }
      .cards-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr) !important;
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
      .metric-card.metric-avoid-db {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
      }
      .metric-card.metric-retrieval {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
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
      .aux-line {
        font-size: 12px;
        color: #5f6368;
        margin: 4px 0 0 0;
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
      .meta-line {
        font-size: 12px;
        color: #5f6368;
        margin-top: 8px;
      }
    </style>
    </head>
    <body>
      <div class="metrics-container">
        <div class="header">
          <h2>Run: Fetch Existing Customer Credit Card Details</h2>
        </div>
        <p class="subtitle" style="color: #EA4335;">Below target ≥90% on at least one metric (Avoid DB: 0.0%, Retrieval: 0.0%).</p>
        <div class="cards-grid">
          <!-- Left card: Avoid DB call accuracy -->
          <div class="metric-card metric-avoid-db">
            <div class="value-line">
              <span class="main-value">0.0%</span>
              <span class="range-tag">Range: (—)</span>
            </div>
            <p class="metric-name">Accuracy of avoiding database call</p>
            <p class="aux-line">0/0 rows</p>
            <div class="target-line">
              <p class="target-info">Target: ≥90%</p>
              <div class="status-icon">❌</div>
            </div>
          </div>
          <!-- Right card: Retrieval accuracy -->
          <div class="metric-card metric-retrieval">
            <div class="value-line">
              <span class="main-value">0.0%</span>
              <span class="range-tag">Range: (0.0% - 0.0%)</span>
            </div>
            <p class="metric-name">Accuracy of card retrieval</p>
            <p class="aux-line">0/3 rows</p>
            <div class="target-line">
              <p class="target-info">Target: ≥90%</p>
              <div class="status-icon">❌</div>
            </div>
            <div class="meta-line">Mode: Strict (Exact match)</div>
          </div>
        </div>
      </div>
    </body>
    </html>
    