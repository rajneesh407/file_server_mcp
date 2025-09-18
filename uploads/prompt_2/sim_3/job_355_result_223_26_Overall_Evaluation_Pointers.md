
        <h2 style="color: #2c3e50; font-size: 28px; margin-bottom: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Pointers for Prompts Improvement</h2>
        <p style="margin-bottom: 15px; color: #34495e; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">This section outlines the suggested areas for improvement for each evaluated prompt.</p>
        <hr style="border-top: 2px solid #bdc3c7; margin: 25px 0;">
        <hr style='border-top: 2px solid #bdc3c7; margin: 25px 0;'>
            <button class="collapsible" style="background-color: #f39c12; color: white; cursor: pointer; padding: 18px; width: 100%; border: none; text-align: left; outline: none; font-size: 18px; font-weight: bold; transition: background-color 0.3s ease; border-radius: 8px; margin-bottom: 5px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <strong style="color: white;">Customer Intent Classification Prompt</strong> (Readiness: 66.67%)
            </button>
            <div class="content" style="padding: 0 18px; max-height: 0; overflow: hidden; transition: max-height 0.3s ease-out; background-color: #ecf0f1; border-radius: 8px; margin-bottom: 10px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <h3 style="color: #2c3e50; font-size: 20px; margin-top: 20px; margin-bottom: 10px;">Overall Readiness Score: 66.67%</h3>
                <p style="margin-bottom: 10px; color: #34495e;">Based on a thorough analysis of the prompt, here are few of the identified issues:

- "3.1.1. Correct any misspelled words for TouchTone."
- "You have to complete the task for given customer utterance with utmost precision."
- 'You will not be penalized for classifying something as "ÖUT OF CONTEXT" if input does not fit any other Intents.'
- "Step 4.3.1. **Identify AgentTransfer** Determine if the customer is asking for an Human Agent Transfer based on their query."
- "Step 4.3.2. **Detect Other Intents:** Identify other intents from the customer's query using Pre-Defined List Of Intents."
- "Step 4.4.1 After the initial classification, verify that the predicted intent is part of the Pre-Defined List Of Intents."
- "4.4.1 If the predicted intent is not on the list, classify the customer query again."
- "Only one example is present in the prompt, under the section **Example 1:**."
- "**Example 1:** only covers a straightforward, unambiguous scenario ('I need to activate my new credit card.')"</p>
            </div>
            <hr style='border-top: 2px solid #bdc3c7; margin: 25px 0;'>
        <script>
            var coll = document.getElementsByClassName("collapsible");
            var i;

            for (i = 0; i < coll.length; i++) {
                coll[i].addEventListener("click", function() {
                    var content = this.nextElementSibling;
                    if (content.style.maxHeight && content.style.maxHeight !== "0px"){
                        content.style.maxHeight = "0"; // Collapse it
                    } else {
                        content.style.maxHeight = content.scrollHeight + "px"; // Expand it
                    }
                });
            }
        </script>
        