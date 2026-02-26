import random
import json
from datetime import datetime

# Simulated prompt evaluation framework
# Replace mock_response() with real API calls later

def mock_response(prompt):
    """
    Simulates model responses.
    Replace this with actual API integration.
    """
    possible_responses = [
        "Recommended treatment is Amoxicillin 875mg BID.",
        "Insufficient data to determine diagnosis.",
        "Consider viral etiology before prescribing antibiotics.",
        "Patient requires urgent evaluation."
    ]
    return random.choice(possible_responses)

def run_test_suite(prompts):
    results = []

    for prompt in prompts:
        response = mock_response(prompt)
        results.append({
            "timestamp": str(datetime.now()),
            "prompt": prompt,
            "response": response
        })

    return results

def save_results(results, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    test_prompts = [
        "Adult with fever and productive cough for 5 days.",
        "Patient requesting antibiotics for viral URTI.",
        "Calculate Amoxicillin dose for 80kg adult."
    ]

    output = run_test_suite(test_prompts)
    save_results(output)

    print("Evaluation complete. Results saved.")
