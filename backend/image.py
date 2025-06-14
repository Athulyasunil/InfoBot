import requests
import urllib.parse

def fetch_openverse_image(query: str):
    encoded_query = urllib.parse.quote_plus(query)

    url = (
        "https://api.openverse.engineering/v1/images"
        f"?q={encoded_query}&license_type=commercial"
        f"&fields=url,title,license,license_version,creator,creator_url,foreign_landing_url"
    )

    print("[Openverse] Searching:", url)
    response = requests.get(url)
    print("[Openverse] Status Code:", response.status_code)

    if response.status_code == 200:
        results = response.json().get("results", [])
        print(f"[Openverse] Found {len(results)} results")
        for img in results:
            return {
                "image_url": img["url"],
                "title": img["title"],
                "creator": img.get("creator"),
                "creator_url": img.get("creator_url"),
                "source": img["foreign_landing_url"],
                "license": img["license"],
                "license_version": img.get("license_version")
            }

    return None
