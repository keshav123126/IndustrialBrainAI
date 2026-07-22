import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

models = [
    "models/gemini-2.0-flash",
    "models/gemini-2.0-flash-001",
    "models/gemini-flash-latest",
    "models/gemini-3.5-flash"
]

for model_name in models:

    try:

        print(f"\nTesting {model_name}")

        response = client.models.generate_content(
            model=model_name,
            contents="Say hello."
        )

        print("SUCCESS")
        print(response.text)

    except Exception as e:

        print("FAILED")
        print(e)