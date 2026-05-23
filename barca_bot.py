import requests
import anthropic
import os
from datetime import datetime

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

def get_barca_news():
    url = "https://gnews.io/api/v4/search"
    params = {
        "q": "FC Barcelona",
        "lang": "en",
        "max": 8,
        "token": os.environ["GNEWS_TOKEN"]
    }
    r = requests.get(url, params=params)
    articles = r.json().get("articles", [])
    return articles

def summarize_news(articles):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    news_text = ""
    for i, a in enumerate(articles, 1):
        news_text += f"{i}. {a['title']}\n{a['description']}\n\n"
    
    today = datetime.now().strftime("%A %d %B %Y")
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""أ
