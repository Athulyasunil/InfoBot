from serpapi import GoogleSearch
import os

def get_top_3_urls(query: str) -> list[str]:
    search = GoogleSearch({
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY")
    })
    results = search.get_dict()
    urls = [r["link"] for r in results.get("organic_results", [])[:3]]
    return urls
