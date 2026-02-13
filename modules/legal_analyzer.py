class LegalAnalyzer:

    @staticmethod
    def classify_charge(charge_text: str) -> str:
        text = charge_text.lower()

        if "input tax credit" in text or "itc" in text:
            return "ITC Reversal Issue"

        elif "best judgment" in text:
            return "Procedural Misuse - Best Judgment"

        elif "time limit" in text or "delay" in text:
            return "Time of Supply / Interest Issue"

        elif "show cause notice" in text:
            return "Threat of SCN - Section 74"

        else:
            return "General GST Dispute"
