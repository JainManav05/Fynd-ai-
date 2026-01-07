import json

# Zero-shot Prompt
ZERO_SHOT_PROMPT = """
You are an expert sentiment analyzer. 
Predict the star rating (1-5) for the following review. 
Return the result in this JSON format:
{
  "predicted_stars": <int>,
  "explanation": "<string>"
}

Review: "{review}"
"""

# Rubric-based Prompt
RUBRIC_PROMPT = """
You are an expert sentiment analyzer. 
Review the following rubric to determine the star rating (1-5).

Rubric:
1 Star: Extremely negative, angry, mentions severe issues, "never coming back".
2 Stars: Mostly negative, disappointed, significant complaints but maybe one minor positive or neutral point.
3 Stars: Mixed, average, "okay", verified complaints balanced with some positives.
4 Stars: Mostly positive, good experience, minor complaints or suggestions for improvement.
5 Stars: Excellent, highly satisfied, glowing praise, "highly recommend".

Predict the star rating based on the rubric.
Return the result in this JSON format:
{
  "predicted_stars": <int>,
  "explanation": "<string>"
}

Review: "{review}"
"""

# Self-reasoning Prompt (Chain of Thought)
REASONING_PROMPT = """
You are an expert sentiment analyzer. 
Analyze the review step-by-step before assigning a rating.

1.  Identify whether the tone is positive, negative, or neutral.
2.  List specific praises and specific complaints.
3.  Weigh the praises against the complaints to determine the overall sentiment.
4.  Assign a star rating (1-5) based on the overall sentiment.

Return the result in this JSON format:
{
  "predicted_stars": <int>,
  "explanation": "<string>"
}

Review: "{review}"
"""
