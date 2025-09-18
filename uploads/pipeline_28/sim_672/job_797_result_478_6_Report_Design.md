
    ##### Purpose
    This chart analyzes the distribution of semantic similarity scores across different attack dimensions for credit card intents. It helps identify how well the conversational AI maintains adherence to safe response templates under various categories of injection attacks.

    ##### Process
    * Filters data to include only credit card intents.
    * Groups response samples by attack dimension categories detailing types of injection attempts.
    * Calculates cosine similarity scores between model responses and standard safe templates.
    * Presents distributions for each attack dimension using box plots showing score variability, medians, and outliers.
    * Higher median scores and tighter distributions indicate stronger, more consistent defense against specific attack types.

    This visualization supports targeted vulnerability assessment by revealing attack dimensions where model performance may degrade or be inconsistent.
    