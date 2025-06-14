import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
for model in genai.list_models():
    print(f"Name: {model.name}")
    print(f"  Display Name: {model.display_name}")
    print(f"  Description: {model.description}")
    print(f"  Input Token Limit: {model.input_token_limit}")
    print(f"  Output Token Limit: {model.output_token_limit}")
    print(f"  Supported Generation Methods: {', '.join(model.supported_generation_methods)}")
    print("-" * 50)
model = genai.GenerativeModel("gemini-2.0-flash-lite-001")

def summarize_with_gemini(content: str, query: str):
    prompt = f"Summarize the following text based on the question: '{query}':\n\n{content}"
    
    response = model.generate_content(prompt)

    return response.text.strip()
