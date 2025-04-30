# tests/test_parser.py
import pytest
from app.scraper.parser import extract_info

def test_extract_info():
    sample_html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Main Heading</h1>
            <p>This is a paragraph.</p>
            <a href="https://link.com">Link</a>
        </body>
    </html>
    """
    data = extract_info(sample_html)
    assert data["title"] == "Test Page"
    assert data["headings"] == ["Main Heading"]
    assert data["paragraphs"] == ["This is a paragraph."]
    assert data["links"] == ["https://link.com"]