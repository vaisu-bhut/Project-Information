# app/main.py
import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import scrape

# Set WindowsProactorEventLoopPolicy for Playwright compatibility
if asyncio.get_event_loop_policy().__class__.__name__ != "WindowsProactorEventLoopPolicy":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI(title="Web Scraper API")
app.include_router(scrape.router)
app.mount("/static", StaticFiles(directory="static"), name="static")  # Serve frontend files

@app.get("/")
async def root():
    return {"message": "Go to /static/index.html to use the scraper"}