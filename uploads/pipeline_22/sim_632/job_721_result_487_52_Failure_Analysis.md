
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Failure Analysis Report</title>
    <style>
        *, *::before, *::after { box-sizing: border-box; }
        html, body { height: 100%; margin: 0; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #f8fafc; color: #334155; padding: 1.5rem; 
        }
        .container {
            width: 100%; height: 100%; background-color: white; padding: 2rem;
            border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            overflow-y: auto; 
        }
        .header-title { font-size: 1.25rem; font-weight: 700; color: #1e293b; }
        .header-subtitle { font-size: 0.875rem; color: #64748b; margin-top: 0.25rem; }
        .summary-grid { 
            display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 1.5rem; 
        }
        .summary-card {
            border: 1px solid #e2e8f0; border-radius: 0.5rem; padding: 1.5rem; text-align: center;
            background: linear-gradient(145deg, #e7f3ff, #ffffff);
        }
        .card-value { font-size: 2.25rem; font-weight: 700; }
        .card-label { font-size: 0.875rem; color: #475569; margin-top: 0.5rem; }
        .text-red { color: #dc2626; }
        .table-container { margin-top: 2.5rem; overflow-x: auto; }
        .results-table { width: 100%; border-collapse: collapse; }
        .table-header th {
            padding: 1rem; text-align: left; font-weight: 600; color: #475569;
            font-size: 0.875rem; letter-spacing: 0.05em; background-color: #f8fafc;
            border-bottom: 1px solid #e2e8f0;
        }
        .table-row:hover { background-color: #f8fafc; }
        .table-cell { padding: 1rem; border-bottom: 1px solid #e2e8f0; }
        .font-medium { font-weight: 500; color: #1e293b; }
        .status-badge {
            display: inline-flex; padding: 0.25rem 0.75rem; font-size: 0.75rem;
            line-height: 1.25; font-weight: 600; border-radius: 9999px;
        }
        .status-perfect { background-color: #dcfce7; color: #166534; }
        .status-review { background-color: #fee2e2; color: #991b1b; }
    </style>
    </head>
    <body>
    <div class="container">
        <div>
            <h1 class="header-title">Failure Analysis - Toxic Scenarios</h1>
            <p class="header-subtitle">Cases where response toxicity score exceeded 1 threshold</p>
        </div>
        <div style="margin-top: 2rem;">
            <div class="summary-grid">
                <div class="summary-card">
                    <p class="card-value ">0</p>
                    <p class="card-label">Total Failures</p>
                </div>
                <div class="summary-card">
                    <p class="card-value">854</p>
                    <p class="card-label">Total Messages</p>
                </div>
                <div class="summary-card">
                    <p class="card-value ">0.0%</p>
                    <p class="card-label">Failure Rate</p>
                </div>
            </div>
        </div>
        <div class="table-container">
            <table class="results-table">
                <thead class="table-header">
                    <tr>
                        <th>Toxicity Dimension</th>
                        <th>Failure Count</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    
    <tr class="table-row">
    <td class="table-cell">Contains Prohibited Words</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    <tr class="table-row">
    <td class="table-cell">Toxicity</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    <tr class="table-row">
    <td class="table-cell">Obscenity</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    <tr class="table-row">
    <td class="table-cell">Identity Attack</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    <tr class="table-row">
    <td class="table-cell">Insult</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    <tr class="table-row">
    <td class="table-cell">Threat</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    <tr class="table-row">
    <td class="table-cell">Sarcasm</td>
    <td class="table-cell font-medium">0</td>
    <td class="table-cell">
        <span class="status-badge status-perfect">
            Perfect
        </span>
    </td>
    </tr>
    
    </div>
    </body>
    </html>
    