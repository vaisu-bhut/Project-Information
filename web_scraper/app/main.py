# app/main.py
import asyncio
from fastapi import FastAPI
from app.routes import scrape

# Set event loop policy for Windows compatibility (optional if server is Linux)
if asyncio.get_event_loop_policy().__class__.__name__ != "WindowsProactorEventLoopPolicy":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI(title="Web Scraper API")
app.include_router(scrape.router)