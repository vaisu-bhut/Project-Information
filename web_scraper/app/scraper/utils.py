import logging
from app.config import LOG_LEVEL

logging.basicConfig(filename='logs/scraper.log', level=LOG_LEVEL)

def clean_text(text: str) -> str:
    return text.strip().replace('\n', ' ')