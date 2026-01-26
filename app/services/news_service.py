import requests


def fetch_top_headlines(api_key: str, country: str, category: str | None, page_size: int):
   
    url = 'https://newsapi.org/v2/top-headlines'
    
    params = {'country': country, 'pageSize': page_size}
    if category:
        params['category'] = category
    
    headers = {'X-Api-Key': api_key}
    
    response = requests.get(url, headers=headers, params=params, timeout=10)
    return response


def fetch_search_results(
    api_key: str,
    query: str,
    page_size: int, 
    sort_by: str = 'publishedAt', 
    language: str = 'en'
    ):
   
    url = 'https://newsapi.org/v2/everything'
    
    params = {
        'q': query,
        'pageSize': page_size,
        'sortBy': sort_by,
        'language': language
    }
    
    headers = {'X-Api-Key': api_key}
    
    response = requests.get(url, headers=headers, params=params, timeout=10)
    return response


def clean_articles(articles: list[dict]) -> list[dict]:
    return [
        {
            'title': article.get('title'),
            'source': (article.get('source') or {}).get('name'),
            'publishedAt': article.get('publishedAt'),
            'url': article.get('url'),
            'description': article.get('description'),
        }
        for article in articles
    ]