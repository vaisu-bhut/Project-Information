# app/scraper/fetcher.py
import requests
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from urllib.parse import urljoin, urlparse
from app.config import REQUEST_TIMEOUT
import asyncio
import random

async def fetch_static(url: str) -> str:
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    return response.text

async def fetch_dynamic(url: str) -> dict:
    """Fetch and crawl all internal pages with Cloudflare bypass."""
    base_domain = urlparse(url).netloc
    visited = set()
    pages_data = {}
    to_crawl = [url]

    async with async_playwright() as p:
        # Optional proxy (uncomment and configure if using)
        # proxy = {"server": "http://your-proxy-host:port", "username": "your-username", "password": "your-password"}
        browser = await p.chromium.launch(headless=True)  # Add proxy=proxy if using
        page = await browser.new_page()
        await stealth_async(page)  # Apply stealth for Cloudflare bypass

        try:
            while to_crawl:
                current_url = to_crawl.pop(0)
                if current_url in visited or not current_url.startswith(f"https://{base_domain}"):
                    continue
                visited.add(current_url)

                try:
                    await page.goto(current_url, wait_until="domcontentloaded", timeout=60000)
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")  # Simulate human behavior
                    await asyncio.sleep(2)  # Wait for JS content
                    html = await page.content()
                    pages_data[current_url] = html
                    print(f"Scraped: {current_url} ({len(visited)} pages total)")  # Log progress

                    # Find all links
                    links = await page.eval_on_selector_all("a[href]", "elements => elements.map(el => el.href)")
                    for link in links:
                        absolute_url = urljoin(current_url, link)
                        if absolute_url not in visited and base_domain in urlparse(absolute_url).netloc:
                            to_crawl.append(absolute_url)
                except Exception as e:
                    print(f"Error fetching {current_url}: {e}")
                await asyncio.sleep(random.uniform(1, 3))  # Random delay to avoid rate limits
        finally:
            await browser.close()

    return pages_data