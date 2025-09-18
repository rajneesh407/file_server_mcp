
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 24px;
        }
        .metrics-container h2 {
            font-size: 20px;
            font-weight: 600;
            color: #1c2a4e;
            margin-top: 0;
            margin-bottom: 20px;
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
        }
        .metric-card {
            border: 1px solid #cde4fe;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            background: linear-gradient(145deg, #e7f3ff, #f8faff);
        }
        .metric-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        .value-line {
            margin-bottom: 8px;
        }
        .main-value {
            font-size: 36px;
            font-weight: 600;
            color: #0d6efd;
        }
        .metric-name {
            font-size: 15px;
            font-weight: 500;
            color: #5f6368;
            margin: 0;
            flex-grow: 1;
            line-height: 1.4;
        }
        .range-line {
            margin-top: 16px;
        }
        .range-tag {
            background-color: #e8eaed;
            color: #3c4043;
            font-size: 12px;
            font-weight: 500;
            padding: 4px 10px;
            border-radius: 12px;
        }
        @media (max-width: 640px) {
            .cards-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    </head>
    <body>
    <div class="metrics-container">
        <h2>Out Of Scope Statistics</h2>
        <div class="cards-grid">
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">97.6%</span>
        </div>
        <p class="metric-name">Cosine Similarity Agreement Rate (NLP/ML Algorithms)</p>
        <div class="range-line">
            <span class="range-tag">Range: 50.0% - 100.0%</span>
        </div>
    </div>
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">99.6%</span>
        </div>
        <p class="metric-name">Cosine Similarity Stability Rate (NLP/ML Algorithms)</p>
        <div class="range-line">
            <span class="range-tag">Range: 90.6% - 100.0%</span>
        </div>
    </div>
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">97.6%</span>
        </div>
        <p class="metric-name">Answer Relevancy Agreement Rate (LLM as a Judge)</p>
        <div class="range-line">
            <span class="range-tag">Range: 50.0% - 100.0%</span>
        </div>
    </div>
            
    <div class="metric-card">
        <div class="value-line">
            <span class="main-value">99.6%</span>
        </div>
        <p class="metric-name">Answer Relevancy Stability Rate (LLM as a Judge)</p>
        <div class="range-line">
            <span class="range-tag">Range: 90.6% - 100.0%</span>
        </div>
    </div>
        </div>
    </div>
    </body>
    </html>
    