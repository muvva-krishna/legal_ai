class PostProcessor:

    @staticmethod
    def clean_response(text: str) -> str:
        return text.replace("**", "").replace("##", "").strip()
