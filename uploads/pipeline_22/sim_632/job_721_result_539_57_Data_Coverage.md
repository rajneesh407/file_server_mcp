
    <html>
    <head>
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #f8f9fa;
        margin: 0;
        padding: 20px;
    }
    .coverage-container {
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        padding: 24px;
        background: #fff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        width: 100%;
        box-sizing: border-box; 
    }
    .coverage-header h2 {
        font-size: 20px;
        font-weight: 600;
        margin: 0 0 4px 0;
    }
    .coverage-subtitle {
        font-size: 14px;
        color: #555;
        margin-bottom: 24px;
    }
    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
    .card {
        text-align: center;
        border-radius: 10px;
        padding: 24px;
        font-weight: 500;
        font-size: 14px;
        border: 1px solid transparent;
    }
    .card span {
        display: block;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .card-total {
        background: #eaf2ff;
        color: #0056D2;
        border-color: #b3d1ff;
    }
    .card-categories {
        background: #eaf2ff;
        color: #1e7e34;
        border-color: #b8e6c6;
    }
    .card-avg {
        background: #eaf2ff;
        color: #e67e22;
        border-color: #ffedbb;
    }
    </style>
    </head>
    <body>
            <div class="coverage-header">
            </div>
            <div class="cards">
                <div class="card card-total">
                    <span>963</span>
                    Total Messages
                </div>
                <div class="card card-categories">
                    <span>10</span>
                    Total Attack Dimensions
                </div>
                <div class="card card-avg">
                    <span>96</span>
                    Avg Messages / Category
                </div>
            </div>
        </div>
    </body>
    </html>
    