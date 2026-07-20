from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview",
    "gemini-2.0-flash",
    "gemini-2.0-flash-001",
]

for model in models:
    print(f"\nTesting {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Say hello."
        )
        print("SUCCESS")
        print(response.text)
        break

    except Exception as e:
        print("FAILED:", e)