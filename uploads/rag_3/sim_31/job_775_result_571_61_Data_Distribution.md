
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
        font-size: 20px;
        color: #1c2a4e;
        font-weight: 600;
        margin: 0 0 6px 0;
      }
      .header-subtitle {
        font-size: 14px;
        color: #5f6368;
        font-weight: 400;
        margin-bottom: 24px;
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
      .card-total {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #ffc107; /* Amber */
      }
      .card-no-query {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #1a9850; /* Green */
      }
      .card-query {
        background: linear-gradient(145deg, #e7f3ff, #ffffff);
        border-left: 5px solid #007bff; /* Blue */
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
      .metric-subtext {
        font-size: 12px;
        color: #5f6368;
        margin-top: 6px;
      }
    </style>
    </head>
    <body>
      <div class="dashboard-container">
        <div class="header-title">Run: Fetch Existing Customer Credit Card Details</div>
        <p class="header-subtitle">Overview of message mix by DB need</p>
        <div class="metrics-grid">
          <div class="metric-card card-total">
            <div class="metric-icon">✉️</div>
            <span class="metric-number">100</span>
            <div class="metric-label">Total User Messages</div>
          </div>
          <div class="metric-card card-no-query">
            <div class="metric-icon">🟢</div>
            <span class="metric-number">50</span>
            <div class="metric-label">Messages not requiring database call</div>
            <div class="metric-subtext">50.0% of total</div>
          </div>
          <div class="metric-card card-query">
            <div class="metric-icon">📂</div>
            <span class="metric-number">50</span>
            <div class="metric-label">Messages requiring database call</div>
            <div class="metric-subtext">50.0% of total</div>
          </div>
        </div>
      </div>
    </body>
    </html>
    