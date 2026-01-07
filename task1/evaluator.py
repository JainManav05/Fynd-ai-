import json
import re
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

def parse_llm_output(output_text):
    """
    Parses LLM output to extract JSON.
    Handles potential markdown blocks.
    """
    try:
        # Remove markdown code blocks if present
        cleaned_text = re.sub(r'```json\s*|\s*```', '', output_text, flags=re.IGNORECASE).strip()
        data = json.loads(cleaned_text)
        return data
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return {"predicted_stars": None, "explanation": "Failed to parse JSON"}

def evaluate_predictions(true_stars, predicted_stars):
    """
    Calculates accuracy and generates a report.
    """
    # Filter out failures (None)
    valid_indices = [i for i, p in enumerate(predicted_stars) if p is not None]
    
    y_true = [true_stars[i] for i in valid_indices]
    y_pred = [predicted_stars[i] for i in valid_indices]
    
    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    
    return acc, report

def save_results(reviews, true_stars, predictions, filename="results.csv"):
    """
    Saves the results to a CSV file.
    """
    df = pd.DataFrame({
        "review": reviews,
        "true_stars": true_stars,
        "predicted_stars": [p.get("predicted_stars") for p in predictions],
        "explanation": [p.get("explanation") for p in predictions]
    })
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")
