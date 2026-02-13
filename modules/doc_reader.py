from docx import Document


class DocumentReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        document = Document(self.file_path)
        full_text = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                full_text.append(paragraph.text.strip())

        return "\n".join(full_text)
