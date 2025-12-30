"""A simple news fetching automation script using NewsAPI.org"""
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    print("Error: API_KEY not set.")
    raise SystemExit(1)

# BASE URL (We will append specific endpoints dynamically)
BASE_URL = "https://newsapi.org/v2/"

def get_articles_by_category(news_category):
    """Fetches top headlines based on category."""
    endpoint = f"{BASE_URL}top-headlines"

    query_parameters = {
        "apiKey": API_KEY,
        # API requires categories to be lowercase (e.g., 'sports', not 'Sport')
        "category": news_category.lower()
    }

    # NOTE: 'sortBy' is NOT allowed for top-headlines, so it was removed.
    return _get_articles(endpoint, query_parameters)

def get_articles_by_query(query):
    """Fetches articles based on a search query using the 'everything' endpoint."""
    # We switch to the 'everything' endpoint because it allows 'sortBy'
    endpoint = f"{BASE_URL}everything"

    query_parameters = {
        "apiKey": API_KEY,
        "q": query,
        "sortBy": "popularity",
        "language": "en",
    }

    # NOTE: The 'everything' endpoint does NOT support the 'country' param.
    return _get_articles(endpoint, query_parameters)

def _get_articles(url, params):
    """Helper function to fetch articles from NewsAPI."""
    response = requests.get(url, params=params, timeout=10)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"NewsAPI error {response.status_code}: {response.json().get('message')}")
        return []

    resp_json = response.json()
    articles = resp_json.get('articles', [])

    if not articles:
        print("No articles found.")
        return []

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 80 + "\n")

if __name__ == "__main__":
    category = input("Enter the news category (e.g., sports, business, technology): ").lower()
    print(f"Getting news for {category}...\n")
    # This will now auto-convert 'Sport' to 'sport' (and you must use 'sports')
    get_articles_by_category(category)

    q = input("Enter the search query you want to fetch news for: ")
    print(f"Getting news for {q}...\n")
    get_articles_by_query(q)
