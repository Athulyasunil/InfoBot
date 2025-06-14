import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash-lite-001")
import re

def clean_json_from_markdown(text: str) -> str:
    """
    Remove markdown-style code block from Gemini's JSON response.
    """
    # Remove triple backticks and optional 'json'
    return re.sub(r"^```(?:json)?\n|\n```$", "", text.strip(), flags=re.IGNORECASE)

def summarize_with_gemini(content: str, query: str):
    prompt = f"""
Summarize the following content in response to the question: "{query}".

Then answer:
- Would a relevant image help the user understand the summary?
- If YES, suggest a single keyword or short phrase that best represents the image.

Format your response strictly as JSON:
{{
  "summary": "...",
  "image_need": true/false,
  "image_term": "..."
}}

Content:
\"\"\"
{content}
\"\"\"
    """

    response = model.generate_content(prompt)
    cleaned = clean_json_from_markdown(response.text)

    try:
        data = json.loads(cleaned)
        summary = data.get("summary", "").strip()
        image_need = data.get("image_need", False)
        image_term = data.get("image_term", None)
        return summary, image_need, image_term
    except Exception as e:
        print("[!] Failed to parse Gemini JSON:", e)
        return response.text.strip(), False, None


