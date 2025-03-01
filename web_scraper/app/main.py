# app/main.py
import asyncio
from fastapi import FastAPI
from app.routes import scrape

# Set WindowsProactorEventLoopPolicy for Playwright compatibility
if asyncio.get_event_loop_policy().__class__.__name__ != "WindowsProactorEventLoopPolicy":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI(title="Web Scraper API")
app.include_router(scrape.router)