
    ##### Purpose
    This chart identifies which attack dimensions most successfully bypass defenses within non-credit card intents. It highlights areas where the conversational AI is vulnerable to jailbreak attempts.

    ##### Process
    * Filters data to include only non-credit card intents.
    * Calculates the percentage of responses classified as violations (jailbreak successful) for each attack dimension.
    * Displays a bar chart ranking attack categories by their violation rates.
    * Taller bars correspond to attack dimensions with higher jailbreak success, signaling priority targets for security improvements.

    This visualization supports focused defensive efforts by clearly showing where the model’s safeguards are weakest against malicious prompt exploitation. A perfectly safe model should have 0 values for all attack dimensions.
    