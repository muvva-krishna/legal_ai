from modules.doc_reader import DocumentReader
from modules.charge_extractor import ChargeExtractor
from modules.legal_analyzer import LegalAnalyzer
from modules.ai_engine import AIEngine
from modules.memo_builder import MemoBuilder


def main():

    input_path = "data\\interview_SCN.docx"
    output_path = "output\\generated_reply.docx"

    # Step 1: Read notice
    reader = DocumentReader(input_path)
    text = reader.extract_text()

    # Step 2: Extract charges
    extractor = ChargeExtractor(text)
    charges = extractor.extract_charges()

    analyzer = LegalAnalyzer()
    ai_engine = AIEngine()

    rebuttals = []

    for charge in charges:
        classification = analyzer.classify_charge(charge["charge_text"])

        # 👇 THIS is where generate_rebuttal is called
        ai_response = ai_engine.generate_rebuttal(
            charge["charge_text"],
            classification,charge["charge_number"]
        )

        rebuttals.append({
            "charge_number": charge["charge_number"],
            "analysis": ai_response
        })

    # Step 3: Build Word reply
    builder = MemoBuilder()
    builder.build_memo(rebuttals, output_path)

    print("Reply generated successfully!")


if __name__ == "__main__":
    main()
