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
    
    if not NEWSAPI_KEY:
        raise HTTPException(status_code=500, detail="API key not configured.")
    
    url = 'https://newsapi.org/v2/top-headlines'
    
    params = {'country': country, 'pageSize': page_size}
    if category:
        params['category'] = category
        
    headers = {'X-Api-Key': NEWSAPI_KEY}
    
    r = requests.get(url, headers=headers, params=params)
    data = r.json()
    
    return data
    