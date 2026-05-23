import requests
import os
from datetime import datetime

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

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

def build_report(articles):
    today = datetime.now().strftime("%A %d %B %Y")
    report = "🔵🔴 تقرير برشلونة اليومي\n"
    report += today + "\n"
    report += "=" * 30 + "\n\n"
    for a in articles:
        report += "📰 " + a["title"] + "\n"
        report += str(a["description"]) + "\n"
        report += "🔗 " + a["url"] + "\n\n"
    report += "⏰ يصلك يوميا الساعة 4 عصراً"
    return report

def send_telegram(text):
    url = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

if __name__ == "__main__":
    articles = get_barca_news()
    report = build_report(articles)
    send_telegram(report)
    print("تم!")
