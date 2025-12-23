import google.generativeai as genai
from core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_text(prompt: str) -> str:
    response = model.generate_content(prompt)

    try:
        text = response.candidates[0].content.parts[0].text
    except Exception as e:
        raise RuntimeError(f"Failed to parse Gemini response: {e}")

    if not text.strip():
        raise RuntimeError("Gemini returned empty text")

    return text.strip()
