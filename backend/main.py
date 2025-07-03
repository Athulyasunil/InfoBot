# main.py
from fastapi import FastAPI
from fastapi import Query
from fastapi import Request
from typing import Optional
from search import get_top_3_urls
from scrape import scrape_article_text
from summarise import summarize_with_gemini
from relevance import rank_articles_by_relevance 
from image import fetch_openverse_image
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://info-bot-ten.vercel.app/"],  # or set to your frontend URL for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
    scraped_contents = [scrape_article_text(url) for url in urls]

    # STEP 3: Rank by relevance
    ranked_articles = rank_articles_by_relevance(query, scraped_contents)

    # STEP 4: Use top 2-3 for summarization
    selected_content = " ".join(ranked_articles[:3])
    summary, content_relevant, image_needed, image_term = summarize_with_gemini(selected_content, query)
    image_info = fetch_openverse_image(image_term) if image_needed and image_term else None
    print("Query:", query)
    print("Summary:", summary)
    print("Content Relevant:", content_relevant)
    print("Image Needed:", image_needed)
    print("Image Term:", image_term)
    return {"summary": summary, "image_info": image_info}
