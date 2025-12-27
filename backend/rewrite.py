import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LLM_ENABLED = GEMINI_API_KEY is not None


if LLM_ENABLED:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("models/gemini-flash-latest")



def build_rewrite_prompt(bio, analysis, target_tone="confident"):
    return f"""
You are helping rewrite a dating app bio.

Original bio:
\"\"\"{bio}\"\"\"

Detected language signals:
- Green flags (positive): {analysis['green_flags']}
- Yellow flags (risky): {analysis['yellow_flags']}
- Red flags (negative): {analysis['red_flags']}
- Explanation keywords: {analysis.get('explanations', {})}

Instructions:
- Keep the original intent.
- Preserve positive traits.
- Reduce or remove dismissive or toxic language.
- Soften dominant tone if present.
- Do NOT invent new personality traits.
- Rewrite the bio in a {target_tone} tone.
- Keep it natural and concise.

Return ONLY the rewritten bio text.
"""



def rewrite_bio_with_gemini(
    bio: str,
    analysis: dict,
    target_tone: str = "confident"
) -> str:
    if not LLM_ENABLED:
        return "LLM rewrite disabled (API key not provided)."

    prompt = build_rewrite_prompt(bio, analysis, target_tone)
    response = model.generate_content(prompt)
    return response.text.strip()
