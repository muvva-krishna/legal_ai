import os
from dotenv import load_dotenv

load_dotenv()

AI_PROVIDER = "gemini"   

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.2
