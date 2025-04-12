# app/model_handler.py
import random

def validate_claim(treatment, policy):
    # Placeholder logic – in reality you'd use OpenAI or HuggingFace here
    if "surgery" in treatment.lower() and "surgery" in policy.lower():
        return {
            'status': 'Valid Claim',
            'confidence': f"{random.randint(85, 95)}%",
            'reason': 'Surgery is covered under policy terms.'
        }
    else:
        return {
            'status': 'Rejected',
            'confidence': f"{random.randint(50, 70)}%",
            'reason': 'Treatment not found in policy terms.'
        }
