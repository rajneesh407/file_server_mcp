
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
            background: linear-gradient(to right, #6a82fb, #fc5c7d); /* Blue gradient background */
            margin: 0;
        }
        .kpi-card {
            background-color: #ffffff;
            background: linear-gradient(145deg, #e7f3ff, #ffffff);
            padding: 25px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            text-align: center; /* Center the text within the card */
            border-left: 5px solid #007bff;
            color: #333; /* Default text color for the card */
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
        <h1>4.0</h1>
        <p>Average Prompt Quality Score</p>
    </div>
    </body>
    </html>
    