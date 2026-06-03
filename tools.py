import logging
import os
import requests
from livekit.agents import function_tool, RunContext
from ddgs import DDGS
from twilio.rest import Client

@function_tool
async def get_weather(context: RunContext, city: str) -> str:
    """Get the current weather for a given city."""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            return response.text.strip()
        return f"Could not retrieve weather for {city}."
    except Exception as e:
        return f"An error occurred while retrieving weather for {city}."

@function_tool
async def search_web(context: RunContext, query: str) -> str:
    """Search the web using DuckDuckGo."""
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if results:
                return "\n".join([f"{r['title']}: {r['body']}" for r in results])
            return "No results found."
    except Exception as e:
        return f"An error occurred while searching for '{query}'."

@function_tool
async def send_whatsapp(context: RunContext, phone_number: str, message: str) -> str:
    """Send a WhatsApp message. Phone number must include country code e.g. +91."""
    try:
        client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        to = phone_number if phone_number.startswith("whatsapp:") else f"whatsapp:{phone_number}"
        msg = client.messages.create(
            from_=os.environ.get("TWILIO_WHATSAPP_NUMBER", "whatsapp:+14155238886"),
            to=to,
            body=message
        )
        return f"Message sent to {phone_number} successfully."
    except Exception as e:
        logging.error(f"Error sending WhatsApp message: {e}")
        return f"Failed to send message to {phone_number}: {e}"

@function_tool
async def get_news(context: RunContext, topic: str) -> str:
    """Get the latest news headlines for a given topic."""
    try:
        url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&pageSize=3&apiKey={os.environ.get('NEWS_API_KEY')}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok" and data["articles"]:
            headlines = [f"{a['title']} from {a['source']['name']}" for a in data["articles"][:3]]
            return ". Next, ".join(headlines)
        return f"No news found for {topic}."
    except Exception as e:
        return f"An error occurred while fetching news for {topic}."
