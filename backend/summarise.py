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
You are a helpful assistant. A user has asked a question: "{query}".

You are given content to summarize based on this question. If the content is relevant, summarize it.

**If the content is not relevant to the query**, ignore it and answer the query using your own knowledge.

Then decide whether an image would significantly improve understanding. 
Only suggest an image if it adds clear educational or visual value.

Respond in this **strict JSON format**:

{{
  "summary": "<summary of relevant content or direct answer>",
  "content_relevant": true/false,
  "image_needed": true/false,
  "image_term": "<relevant search keyword, or null if image_needed is false>"
}}

Here is the content:
\"\"\"
{content}
\"\"\"
"""

    response = model.generate_content(prompt)
    cleaned = clean_json_from_markdown(response.text)

    try:
        data = json.loads(cleaned)
        summary = data.get("summary", "").strip()
        content_relevant = data.get("content_relevant", False)
        image_needed = data.get("image_needed", False)
        image_term = data.get("image_term", None)
        return summary, content_relevant, image_needed, image_term
    except Exception as e:
        print("[!] Failed to parse Gemini JSON:", e)
        return response.text.strip(), False, None


