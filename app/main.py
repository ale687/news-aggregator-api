import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import requests


load_dotenv()


NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")


app = FastAPI(title='News Aggregator API')


@app.get('/health')
def health():
    return {'status': 'ok'} 


@app.get('/news/top')
def top_headlines(country: str = 'ar', category: str | None = None, page_size: int = 10):
    """
    Fetch top news headlines from NewsAPI.
    Supports optional filtering by category, country, and page size.
    """
    
    # Validate API key
    if not NEWSAPI_KEY:
        raise HTTPException(status_code=500, detail="API key not configured.")
    
    # build request
    url = 'https://newsapi.org/v2/top-headlines'
    
    params = {'country': country, 'pageSize': page_size}
    if category:
        params['category'] = category
        
    headers = {'X-Api-Key': NEWSAPI_KEY}
    
    # call NewsAPI
    r = requests.get(url, headers=headers, params=params, timeout=10)
    
    # Handle errors returned by the external News API
    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=r.text)
    
    # Parse external API response
    data = r.json()
    articles = data.get('articles', [])
    
    # Transform and clean articles data
    clean_articles = [
        {
            'title': article.get('title'),
            'source': (article.get('source') or {}).get('name'),
            'publishedAt': article.get('publishedAt'),
            'url': article.get('url'),
        }
        for article in articles
    ]
    
    # Transform and clean articles data
    return {
        'totalResults': data.get('totalResults'),
        'articles': clean_articles
    }
    