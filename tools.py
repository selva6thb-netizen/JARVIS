import logging
import os
import requests
import time
from livekit.agents import function_tool, RunContext
from ddgs import DDGS
import pywhatkit
import pyautogui

@function_tool
async def get_weather(
        context: RunContext,  # type: ignore
        city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}."

@function_tool
async def search_web(
        context: RunContext,  # type: ignore
        query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if results:
                output = "\n".join([f"{r['title']}: {r['body']}" for r in results])
                logging.info(f"Search results for '{query}': {output}")
                return output
            return "No results found."
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."

@function_tool
async def send_whatsapp(
        context: RunContext,  # type: ignore
        phone_number: str,
        message: str) -> str:
    """
    Send a WhatsApp message to a phone number.
    Phone number must include country code e.g. +91 for India.
    """
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            wait_time=15,
            tab_close=False
        )
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        return f"Message sent to {phone_number} successfully."
    except Exception as e:
        logging.error(f"Error sending WhatsApp message: {e}")
        return f"Failed to send message to {phone_number}: {e}"

@function_tool
async def get_news(
        context: RunContext,  # type: ignore
        topic: str) -> str:
    """
    Get the latest news headlines for a given topic.
    """
    try:
        url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&pageSize=3&apiKey={os.environ.get('NEWS_API_KEY')}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok" and data["articles"]:
            headlines = []
            for article in data["articles"][:3]:
                headlines.append(f"{article['title']} from {article['source']['name']}")
            result = ". Next, ".join(headlines)
            logging.info(f"News fetched: {result}")
            return result
        else:
            return f"No news found for {topic}."
    except Exception as e:
        logging.error(f"Error fetching news: {e}")
        return f"An error occurred while fetching news for {topic}."