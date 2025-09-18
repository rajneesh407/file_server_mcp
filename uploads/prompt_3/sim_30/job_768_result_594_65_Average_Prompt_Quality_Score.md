
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KPI Card</title>
    <style>
        body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f0f2f5;
        }
        .kpi-card {
            background-color: #ffffff;
            padding: 25px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            text-align: center;
            border-left: 5px solid #007bff;
        }
        .kpi-card h1 {
            font-size: 4em;
            margin: 0;
            color: #333;
        }
        .kpi-card p {
            margin: 0;
            font-size: 1.1em;
            color: #6c757d;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
    </style>
    </head>
    <body>
    <div class="kpi-card">
        <h1>{raw_output['metrics_df']['average_score']}</h1>
        <p>Average Score</p>
    </div>
    </body>
    </html>
    