import os

from pathlib import Path
from dotenv import load_dotenv

from groq import Groq


load_dotenv(
    Path(__file__).resolve().parents[2] / ".env"
)


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found.")


class GeminiClient:

    def __init__(self):

        self.client = Groq(
            api_key=api_key
        )

    def generate(
        self,
        prompt,
        temperature=0.2
    ):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content


gemini = GeminiClient()