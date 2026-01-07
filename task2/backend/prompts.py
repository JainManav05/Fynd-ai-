# Centralized prompts to ensure consistency and reusability
# These align with the requirements for user response, admin summary, and recommended actions.

USER_RESPONSE_PROMPT = """
You are a customer service representative.
Based on the following customer review, draft a polite and empathetic response.
If the review is negative, apologize and offer assistance.
If the review is positive, thank them warmly.

Review: "{review_text}"
Rating: {rating}/5

Response:
"""

ADMIN_SUMMARY_PROMPT = """
Summarize the following customer review in one concise sentence for an admin dashboard.
Focus on the core issue or praise.

Review: "{review_text}"
"""

RECOMMENDED_ACTION_PROMPT = """
Based on the review below, suggest a specific, actionable step the business should take.
Examples: "Refund customer", "Investigate hygiene", "Reward staff member", "No action needed".
Keep it very short (under 5 words).

Review: "{review_text}"
Rating: {rating}/5
"""
