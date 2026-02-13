import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE


class AIEngine:

    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in config.py or .env")

        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def _build_prompt(self, charge_text: str, classification: str, charge_number: int) -> str:
        return f"""
You are drafting a formal legal reply to a GST tax notice.

You must strictly follow the structure shown below.

Charge Number: {charge_number}
Charge Category: {classification}

Allegation Text:
{charge_text}

Return ONLY the following format:

{charge_number}. RE: {classification.upper()}

AI-Generated Analysis & Counter-Argument:

What the Charge Means:
(Explain clearly in 3-4 sentences.)

Our Counter-Argument:
(Provide strong legal rebuttal focusing on procedural defects and burden of proof.)

Legal Support from AI Research:
- Cite relevant CGST/IGST sections
- Mention at least one judicial precedent type

Simple Explanation:
(Explain simply for a business owner.)

Do not add extra commentary.
Do not change structure.
Do not add markdown.
"""

    def generate_rebuttal(self, charge_text: str, classification: str, charge_number: int) -> str:

        prompt = self._build_prompt(charge_text, classification, charge_number)

        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": TEMPERATURE,
                    "top_p": 0.9,
                    "max_output_tokens": 3000
                }
            )

            if not response or not response.text:
                return "AI returned empty response."

            return response.text.strip()

        except Exception as e:
            return f"AI Generation Error: {str(e)}"
