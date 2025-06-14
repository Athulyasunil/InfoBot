import httpx
from bs4 import BeautifulSoup

def scrape_article_text(url: str) -> str:
    try:
        response = httpx.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join(p.get_text() for p in paragraphs)
        return text[:1000]  # Limit to 1500 characters to fit OpenAI limits
    except Exception as e:
        return ""
