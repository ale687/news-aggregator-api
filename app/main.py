import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from app.services.news_service import fetch_top_headlines, fetch_search_results, clean_articles


load_dotenv()


NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")


app = FastAPI(title='News Aggregator API')


@app.get('/health')
def health():
    return {'status': 'ok'} 


@app.get('/news/top')
def top_headlines(country: str = 'us', category: str | None = None, page_size: int = 10):
    """
    Fetch top news headlines from NewsAPI.
    Supports optional filtering by category, country, and page size.
    """
    
    # Validate API key
    if not NEWSAPI_KEY:
        raise HTTPException(status_code=500, detail="API key not configured.")
    
    r = fetch_top_headlines(
        api_key=NEWSAPI_KEY,
        country=country,
        category=category,
        page_size=page_size
    )
    
    # Handle errors returned by the external News API
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    
    data = r.json()
    articles = data.get('articles', [])
    clean = clean_articles(articles)
    
    return {
        'totalResults': data.get('totalResults'),
        'articles': clean
    }
    
    
@app.get('/news/search')
def search_news(q: str, page_size: int = 10, sort_by: str = 'publishedAt', language: str = 'en'):
    """
    Search news articles by keyword using NewsAPI.
    """
    
    # Validate inputs
    if not q.strip():
        raise HTTPException(status_code=400, detail="Query parameter 'q' cannot be empty.")

    # Validate API key
    if not NEWSAPI_KEY:
        raise HTTPException(status_code=500, detail="API key not configured.")    
    
    r = fetch_search_results(
        api_key=NEWSAPI_KEY,
        query=q,
        page_size=page_size,
        sort_by=sort_by,
        language=language
    )
    
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    
    data = r.json()
    articles = data.get('articles', [])
    clean = clean_articles(articles)
    
    return {
        'query': q,
        'totalResults': data.get('totalResults'),
        'articles': clean
    }