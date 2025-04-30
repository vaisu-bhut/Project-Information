# app/routes/scrape.py
from fastapi import APIRouter, WebSocket, HTTPException
from app.models.scrape import ScrapeRequest
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

@router.websocket("/ws/scrape")
async def websocket_scrape(websocket: WebSocket):
    await websocket.accept()
    url = websocket.query_params.get("url")
    if not url:
        await websocket.send_text("Error: No URL provided")
        await websocket.close()
        return

    try:
        pages_data = {}
        batch_size = 5  # Send data every 5 pages
        async for page_url, html in fetch_dynamic(str(url)):  # Use generator-style fetch
            pages_data[page_url] = extract_info(html)
            if len(pages_data) >= batch_size:
                await websocket.send_json(pages_data)
                pages_data.clear()  # Clear after sending
        if pages_data:  # Send any remaining pages
            await websocket.send_json(pages_data)
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")
    finally:
        await websocket.close()