
    <html>
    <head>
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #fff;
        margin: 0;
        padding: 20px;
    }
    .coverage-container {
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        padding: 20px;
        background: #fff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .coverage-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }
    .coverage-header h2 {
        font-size: 18px;
        font-weight: 600;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .coverage-subtitle {
        font-size: 14px;
        color: #555;
        margin-top: 4px;
    }
    .cards {
        display: flex;
        gap: 16px;
    }
    .card {
        flex: 1;
        text-align: center;
        border-radius: 10px;
        padding: 20px;
        font-weight: 500;
    }
    .card span {
        display: block;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .card-total {
        background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        color: #0056D2;
    }
    .card-in-scope {
        background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        color: #008000;
    }
    .card-out-scope {
        background: linear-gradient(145deg, #e7f3ff, #ffffff); /* Soft Blue */
        color: #800080;
    }
    </style>
    </head>
    <body>
        <div class="coverage-header">
                <div>
                    <div class="coverage-subtitle">
                        Testing coverage across dimensions and intent categories
                    </div>
                </div>
            </div>
            <div class="cards">
                <div class="card card-total">
                    <span>96</span>
                    Total User Messages
                </div>
                <div class="card card-in-scope">
                    <span>80</span>
                    In-Scope Messages
                </div>
                <div class="card card-out-scope">
                    <span>16</span>
                    Out-of-Scope Messages
                </div>
            </div>
        </div>
    </body>
    </html>
    