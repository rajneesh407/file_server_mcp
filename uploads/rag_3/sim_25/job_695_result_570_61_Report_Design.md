
    ##### <span style="color:#1f77b4;">📈 Chart Explanation</span><br>
    <strong>Outcome Distribution Among Query Rows (db_call_needed = 1)</strong><br>
    • One stacked bar per intent; values are percentages of query-required rows for that intent.<br>
    • Stack order (top ➜ bottom): <em>No database call</em> <span style="color:#5f6368;">dark gray</span>, <em>Incorrect match</em> <span style="color:#d73027;">red</span>, <em>Contains correct cards</em> <span style="color:#fdae61;">orange</span>, <em>Exact match</em> <span style="color:#1a9850;">green</span>.<br>
    • Labels show “X.Y% (count)” where space permits; labels auto-hide when segments are too small.<br>

    ##### <span style="color:#1f77b4;">🎨 Color Legend</span><br>
    • Exact match: <span style="color:#1a9850;">green</span><br>
    • Contains correct cards: <span style="color:#fdae61;">orange</span><br>
    • Incorrect match: <span style="color:#d73027;">red</span><br>
    • No database call (when data was required): <span style="color:#5f6368;">dark gray</span><br>

    ##### <span style="color:#1f77b4;">🔎 How to Read This Chart</span><br>
    • Higher <strong>Exact match</strong> indicates better retrieval accuracy when a DB call is needed.<br>
    • <strong>Contains correct cards</strong> may be partially acceptable depending on downstream tolerance, but should ideally convert to Exact matches.<br>
    • <strong>Incorrect match</strong> and <strong>No database call</strong> (for query-required rows) are undesirable and should be minimized.<br>
    • Bars are normalized per intent within the query-required group; intents with zero query-required rows will display as empty (0%).<br>
    