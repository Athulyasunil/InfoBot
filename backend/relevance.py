from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_articles_by_relevance(query: str, articles: list[str]) -> list[str]:
    """Ranks articles by relevance to query using TF-IDF cosine similarity"""
    if not articles:
        return []

    # Vectorize query + articles
    corpus = [query] + articles
    tfidf = TfidfVectorizer().fit_transform(corpus)

    # Compute cosine similarity of query to each article
    similarities = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    # Sort articles by similarity descending
    ranked_articles = [article for _, article in sorted(zip(similarities, articles), key=lambda x: x[0], reverse=True)]
    return ranked_articles
