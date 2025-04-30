# tests/test_fetcher.py
import pytest
from app.scraper.fetcher import fetch_static, fetch_dynamic

def test_fetch_static():
    html = fetch_static("https://example.com")
    assert isinstance(html, str)
    assert "<html" in html.lower()  # Basic check for HTML content

def test_fetch_dynamic():
    html = fetch_dynamic("https://example.com")
    assert isinstance(html, str)
    assert "<html" in html.lower()  # Basic check for HTML content