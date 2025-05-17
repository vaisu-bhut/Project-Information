# AI-Powered Web Scraper API & UI 🚀  
*(FastAPI + BeautifulSoup + WebSockets)*  

---

## Table of Contents
1. [Why This Tech Stack?](#why-this-tech-stack)
2. [Features](#features)
3. [API Reference](#api-reference)
4. [WebSocket Streaming](#websocket-streaming)
5. [Frontend](#frontend)
6. [Project Structure](#project-structure)
7. [Roadmap](#roadmap)
8. [Contributing](#contributing)
9. [License](#license)

---

## Why This Tech Stack?
| Layer | Choice | Rationale |
|-------|--------|-----------|
| **API** | **FastAPI** | Async-first, minimal boilerplate, auto-generated OpenAPI docs. |
| **HTML Parsing** | **BeautifulSoup + lxml** | Pythonic, robust, and fast with C-based lxml backend. |
| **Streaming** | **WebSockets** | Delivers parsed data in real-time batches, no polling needed. |

This stack prioritizes simplicity, speed, and reliability—no heavy dependencies or paid tools required.

---

## Features
- **Recursive Crawling** – Follows same-site internal links with throttling to avoid rate limits.  
- **Structured Output** – Extracts titles, headings, paragraphs, lists, and links in JSON format.  
- **Real-Time Streaming** – Pushes JSON batches every 5 pages (configurable) via WebSockets.  
- **User-Friendly Frontend** – Static HTML/JS UI for instant scraping demos.  
- **Extensible Parsing** – Easily swap in custom parsing logic or libraries like newspaper3k.  

---

## API Reference
### `POST /scrape`
Scrape a URL and its internal links.

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `url` | string (valid URL) | ✅ | `"https://example.com"` |

**Sample Response**:
```json
{
  "https://example.com": {
    "title": "Example Domain",
    "headings": ["Example Domain"],
    "paragraphs": ["This domain is for use in illustrative examples..."],
    "lists": { "ordered": [], "unordered": [] },
    "links": ["https://www.iana.org/domains/example"]
  }
}
```

Errors return HTTP status codes with a JSON `detail` field.

---

## WebSocket Streaming
`GET /ws/scrape?url=https://example.com`

- Establishes a WebSocket connection.  
- Server crawls asynchronously, sending JSON batches every 5 pages (default):  
  ```json
  {
    "https://example.com/about": { ... },
    "https://example.com/contact": { ... }
  }
  ```
- Connection closes on crawl completion or error.

---

## Frontend
- **Location**: `static/index.html` + `static/script.js`  
- **Usage**: Paste a URL, view prettified JSON output in the browser.  
- **Purpose**: Enables non-technical users to scrape without coding.

---

## Project Structure
```
web_scraper/
│
├── app/                    # FastAPI backend
│   ├── config.py           # Settings (timeouts, logging)
│   ├── main.py             # Application entry point
│   ├── routes/             # API and WebSocket endpoints
│   └── scraper/            # Parsing and fetching logic
│
├── static/                 # Frontend assets (HTML/JS)
├── tests/                  # pytest test suites
├── requirements.txt
└── run.sh                  # Helper script for venv + server
```

---

## Roadmap
- Add support for custom parsing rules via config files.  
- Implement rate-limit detection and auto-retry logic.  
- Enhance frontend with visualization of scraped data (e.g., link graphs).  

---

## Contributing
Want to improve the project?  
1. Fork the repo and create a feature branch.  
2. Make atomic, well-documented commits.  
3. Run `pre-commit` hooks locally.  
4. Submit a pull request with a clear description of *what* and *why*.  
PRs are squash-merged after CI approval.

---

## License
[MIT](LICENSE) – Free to use, modify, and distribute. Keep the copyright notice.

---

> Crafted by Vasu Bhut – Making web scraping fast, reliable, and painless. ✌️
