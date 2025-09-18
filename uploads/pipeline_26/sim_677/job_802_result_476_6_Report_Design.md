
    ##### Purpose
    This chart analyzes the model’s ability to maintain response safety under injection attacks for credit card intents. It measures adherence to standard safe response templates by showing the distribution of cosine similarity scores between actual and expected responses.

    ##### Process
    * Filters data to include only credit card intents, excluding non-credit card intents.
    * Groups tested samples by similarity score ranges (bins) representing how closely responses match expected safe templates.
    * Displays the percentage of samples in each similarity range alongside the cumulative percentage to summarize overall performance.
    * Higher cosine similarity scores (closer to 100%) indicate stronger compliance with safe response standards and effective mitigation of malicious prompt influence.

    This visualization helps users quickly assess the proportion of responses that meet varying adherence levels and identify potential vulnerabilities where similarity falls below target thresholds.
    