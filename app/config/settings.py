from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

MODEL_NAME = "claude-3-haiku-20240307"
MAX_TOKENS = 200
