# main.py
from fastapi import FastAPI
from fastapi import Query
from fastapi import Request
from typing import Optional
from search import get_top_3_urls
from scrape import scrape_article_text
from summarise import summarize_with_gemini
app = FastAPI()

@app.get("/ask")
async def ask(query: Optional[str] = Query(None)):
    if not query:
        return {"error": "Missing query parameter"}
    
    return {"message": f"You asked: {query}"}


@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    query = data.get("query")

    urls = get_top_3_urls(query)
    content = " ".join([scrape_article_text(url) for url in urls])
    summary = summarize_with_gemini(content, query)

    return {"summary": summary}
