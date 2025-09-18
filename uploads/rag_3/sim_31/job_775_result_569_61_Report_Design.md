
    ##### <span style="color:#1f77b4;">📈 Chart Explanation</span><br>
    <strong>Accuracy of Avoiding Database Call (db_call_needed = 0)</strong><br>
    <ul>
      <li>One stacked bar per intent; values are percentages of no-query rows for that intent.</li>
      <li>Labels show “X.Y% (count)” where space permits; labels auto-hide when segments are too small.</li>
      <li>Some intents may not have user messages that do not require database calls.</li>
    </ul>

    ##### <span style="color:#1f77b4;">🎨 Color Legend</span><br>
    <ul>
      <li>No database call: <span style="color:#1a9850;">green</span></li>
      <li>Database call: <span style="color:#f28e2b;">orange</span></li>
    </ul>

    ##### <span style="color:#1f77b4;">🔎 How to Read This Chart</span><br>
    <ul>
      <li>Higher <strong>No database call</strong> indicates better avoidance behavior when a DB call is not required.</li>
      <li><strong>Database call</strong> reflects unnecessary fetching and should be minimized, but does not necessarily mean the overall chat pipeline will be wrong.</li>
      <li>Bars are normalized per intent within the no-query group; intents with zero no-query rows will display as empty (0%).</li>
    </ul>
    