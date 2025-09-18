
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toxicity Reduction Analysis</title>
    <style>
    * {
    box-sizing: border-box;
    }
    body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background-color: #ffffff;
    color: #212529;
    margin: 0;
    }
    .container {
    padding: 2rem 1rem;
    max-width: 100%;
    }
    .grid {
    display: grid;
    grid-template-columns: repeat(1, minmax(0, 1fr));
    gap: 3rem;
    }
    @media (min-width: 1024px) {
    .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    }
    h1 {
    font-size: 1.875rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 2.5rem;
    }
    h2 {
    font-size: 1.25rem;
    font-weight: 600;
    text-align: center;
    margin-bottom: 1.5rem;
    }
    .table-container {
    overflow-x: auto;
    border: 1px solid #dee2e6;
    border-radius: 0.5rem;
    }
    table {
    width: 100%;
    border-collapse: collapse;
    }
    th, td {
    padding: 1.25rem;
    border-bottom: 1px solid #dee2e6;
    text-align: center;
    vertical-align: middle;
    }
    thead th {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: white;
    }
    tbody tr:last-child th,
    tbody tr:last-child td {
    border-bottom: none;
    }
    .bg-slate-50 { background-color: #f9fafb; }
    .thead-toxic { background-color: #1e3a8a; }
    .thead-nontoxic { background-color: #1e3a8a; }
    .badge {
    display: inline-block;
    padding: 0.35em 0.65em;
    font-size: 0.8em;
    font-weight: 700;
    line-height: 1;
    color: #fff;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 50rem;
    }
    .badge-success { background-color: #d1fae5; color: #065f46; }
    .badge-warning { background-color: #fef3c7; color: #92400e; }
    .badge-danger { background-color: #fee2e2; color: #991b1b; }
    .badge-secondary { background-color: #e5e7eb; color: #374151; }
    </style>
    </head>
    <body>
    <div class="container">
    <h1>☣️ Toxicity Reduction Analysis</h1>
    <div class="grid">
    
    <div>
        <h2 style="color: #c81e1e;">Toxic User Message Scenarios</h2>
        <div class="table-container">
            <table>
                <thead class="thead-toxic">
                    <tr>
                        <th>Dimension</th>
                        <th>Input Score</th>
                        <th>Output Score</th>
                        <th>% Reduced</th>
                    </tr>
                </thead>
                <tbody>
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Contains Prohibited Words</td>
    <td class="p-3 text-sm text-red-600 font-semibold">2.32</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    
    <tr class="bg-slate-50">
    <td class="p-3 text-sm font-medium text-gray-800">Toxicity</td>
    <td class="p-3 text-sm text-red-600 font-semibold">1.78</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Obscenity</td>
    <td class="p-3 text-sm text-red-600 font-semibold">1.62</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    
    <tr class="bg-slate-50">
    <td class="p-3 text-sm font-medium text-gray-800">Identity Attack</td>
    <td class="p-3 text-sm text-red-600 font-semibold">1.53</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Insult</td>
    <td class="p-3 text-sm text-red-600 font-semibold">1.33</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    
    <tr class="bg-slate-50">
    <td class="p-3 text-sm font-medium text-gray-800">Threat</td>
    <td class="p-3 text-sm text-red-600 font-semibold">2.02</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Sarcasm</td>
    <td class="p-3 text-sm text-red-600 font-semibold">1.40</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-success">100.0%</span>
    </td>
    </tr>
    </tbody>
            </table>
        </div>
    </div>
    
    
    <div>
    <h2 style="color: #059669;">Non-Toxic User Message Scenarios</h2>
    <div class="table-container">
    <table>
        <thead class="thead-nontoxic">
            <tr>
                <th>Dimension</th>
                <th>Input Score</th>
                <th>Output Score</th>
                <th>% Reduced</th>
            </tr>
        </thead>
        <tbody>
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Contains Prohibited Words</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    
    <tr class="bg-slate-50">
    <td class="p-3 text-sm font-medium text-gray-800">Toxicity</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Obscenity</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    
    <tr class="bg-slate-50">
    <td class="p-3 text-sm font-medium text-gray-800">Identity Attack</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Insult</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    
    <tr class="bg-slate-50">
    <td class="p-3 text-sm font-medium text-gray-800">Threat</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    
    <tr>
    <td class="p-3 text-sm font-medium text-gray-800">Sarcasm</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3 text-sm text-gray-700">0.00</td>
    <td class="p-3">
        <span class="badge badge-secondary">N/A</span>
    </td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    
    </div>
    </div>
    </body>
    </html>
    