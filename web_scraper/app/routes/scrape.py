# app/routes/scrape.py
from fastapi import APIRouter, HTTPException
from app.models.scrape import ScrapeRequest, ScrapeResponse
from app.scraper.fetcher import fetch_dynamic
from app.scraper.parser import extract_info

router = APIRouter()

@router.post("/scrape", response_model=dict)
async def scrape_url(request: ScrapeRequest):
    try:
        pages_data = await fetch_dynamic(str(request.url))
        result = {}
        for url, html in pages_data.items():
            result[url] = extract_info(html)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scraping failed: {str(e)}")