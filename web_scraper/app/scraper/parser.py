# app/scraper/parser.py
from bs4 import BeautifulSoup

def extract_info(html: str) -> dict:
    """Extract all meaningful sections from HTML."""
    soup = BeautifulSoup(html, 'lxml')
    
    data = {
        "title": soup.title.string.strip() if soup.title else "No Title",
        "headings": [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
        "paragraphs": [p.get_text(strip=True) for p in soup.find_all('p')],
        "lists": {
            "ordered": [[li.get_text(strip=True) for li in ol.find_all('li')] for ol in soup.find_all('ol')],
            "unordered": [[li.get_text(strip=True) for li in ul.find_all('li')] for ul in soup.find_all('ul')]
        },
        "links": [a['href'] for a in soup.find_all('a', href=True)],
        "sections": []
    }

    for section in soup.find_all('div', {'id': True, 'class': True}):
        section_data = {
            "id": section.get('id', ''),
            "class": ' '.join(section.get('class', [])),
            "headings": [h.get_text(strip=True) for h in section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
            "paragraphs": [p.get_text(strip=True) for p in section.find_all('p')],
            "links": [a['href'] for a in section.find_all('a', href=True)]
        }
        if any(section_data[k] for k in ['headings', 'paragraphs', 'links']):
            data["sections"].append(section_data)

    return data