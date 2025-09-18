
        <h2 style="color: #2c3e50; font-size: 28px; margin-bottom: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center;"><strong>Pointers for Prompts Improvement</strong></h2>
        <p style="margin-bottom: 15px; color: #34495e; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">This section outlines the suggested areas for improvement for each evaluated prompt.</p>
        <hr style="border-top: 2px solid #bdc3c7; margin: 25px 0;">
        
            <details style="margin-bottom: 15px; border: 1px solid #ddd; border-radius: 8px; background-color: #fff;">
                <summary style="padding: 18px; font-size: 18px; font-weight: bold; cursor: pointer; outline: none; background-color: #f0f0f0; border-bottom: 1px solid #ddd; border-radius: 8px 8px 0 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                    <span style="color: #f39c12;">Customer Intent Classification Prompt</span> (Readiness: 66.67%)
                </summary>
                <div style="padding: 18px; background-color: #ecf0f1; border-radius: 0 0 8px 8px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                    <h3 style="color: #2c3e50; font-size: 20px; margin-top: 10px; margin-bottom: 10px;">Overall Readiness Score: 66.67%</h3>
                    <p style="margin-bottom: 5px; color: #34495e;">Based on a thorough analysis of the prompt, here are few of the identified issues:

- 3.1.1. Correct any misspelled words for TouchTone.
- 4.3.1. **Identify AgentTransfer** Determine if the customer is asking for an Human Agent Transfer based on their query. 
- 4.4.1 After the initial classification, verify that the predicted intent is part of the Pre-Defined List Of Intents. 
- 4.4.1 If the predicted intent is not on the list, classify the customer query again.
- You will not be penalized for classifying something as "ÖUT OF CONTEXT" if input does not fit any other Intents.
- Only one example is present in the prompt, under **Example 1:**.
- There are no lines in the prompt that instruct the model to avoid toxic, harmful, or offensive responses.
- There are no lines in the prompt that instruct the model to avoid bias or remain unbiased in all scenarios.</p>
                </div>
            </details>
            <hr style='border-top: 2px solid #bdc3c7; margin: 25px 0;'>
            