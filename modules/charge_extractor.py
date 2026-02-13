import re
from typing import List, Dict


class ChargeExtractor:
    def __init__(self, document_text: str):
        self.text = document_text

    def extract_charges(self) -> List[Dict]:
        pattern = r"\n\s*\d+\.\s+(.*?)(?=\n\s*\d+\.|\Z)"
        matches = re.findall(pattern, self.text, re.DOTALL)

        charges = []
        for idx, match in enumerate(matches, start=1):
            charges.append({
                "charge_number": idx,
                "charge_text": match.strip()
            })

        return charges
