# AI-Powered Web Scraper API & UI 🚀  
*(FastAPI + Playwright + BeautifulSoup + WebSockets)*  

> **TL;DR** – Point the API at any public URL and get back clean, structured content (title, headings, paragraphs, lists, links) in near-real time. A glow-up frontend is bundled so non-devs can click-and-scrape.

---

## Table of Contents
1. [Why this tech stack?](#why-this-tech-stack)
2. [Features](#features)
3. [Quick Start](#quick-start)
4. [API Reference](#api-reference)
5. [WebSocket Streaming](#websocket-streaming)
6. [CLI & Frontend](#cli--frontend)
7. [Project Structure](#project-structure)
8. [Testing](#testing)
9. [Roadmap](#roadmap)
10. [Contributing](#contributing)
11. [License](#license)

---

## Why this tech stack?
| Layer | Choice | Rationale |
|-------|--------|-----------|
| **API** | **FastAPI** | Async-first, type-hinted, automatic OpenAPI docs, zero boilerplate. |
| **Browser Automation** | **Playwright (+ playwright-stealth)** | Handles modern, JS-heavy sites; bypasses basic bot detection; headless or headed. |
| **HTML Parsing** | **BeautifulSoup + lxml** | Battle-tested, Pythonic, lightning-fast with C-based lxml backend. |
| **Streaming** | **WebSockets** | Pushes each batch of pages as soon as they’re parsed—no long-polling. |
| **Data Validation** | **Pydantic** | Guarantees request/response schema integrity; autogenerates examples. |
| **Testing** | **pytest + fastapi.testclient** | Fast, minimalist, no external server spin-up. |

These tools maximize developer velocity **and** scraping reliability without adding paid dependencies or heavyweight frameworks.

---

## Features
- **Recursive, Same-Site Crawl** – Follows internal links, throttled to dodge rate limits.  
- **Dynamic Rendering** – Full JS execution via Playwright, so SPAs work.  
- **Incremental Streaming** – Every `n` pages the server pushes a JSON batch over WebSocket.  
- **Extensible Parsers** – Swap in Readability-lxml, newspaper3k, or custom heuristics.  
- **Zero-Config Frontend** – Static HTML/JS UI served from `/static` for plug-and-play demos.  

---

## Quick Start
```bash
# 1. Clone
git clone https://github.com/yourusername/web_scraper.git
cd web_scraper

# 2. Python env
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
playwright install  # download browser drivers

# 3. Run
uvicorn app.main:app --reload           # http://127.0.0.1:8000
# or with the helper script
./run.sh
```
Open <http://127.0.0.1:8000/static/index.html>, paste a URL, and watch the data flow ⚡.

---

## API Reference
### `POST /scrape`
Scrape a single URL **and every internal link**.

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `url` | string (valid URL) | ✅ | `"https://example.com"` |

<details>
<summary>Sample Response</summary>

```json
{
  "https://example.com": {
    "title": "Example Domain",
    "headings": ["Example Domain"],
    "paragraphs": ["This domain is for use in illustrative examples..."],
    "lists": { "ordered": [], "unordered": [] },
    "links": ["https://www.iana.org/domains/example"]
  },
  "...": { }
}
```
</details>

Errors return standard HTTP codes + JSON `detail`.

---

## WebSocket Streaming
`GET /ws/scrape?url=https://example.com`

- Opens a bidirectional channel.
- Server crawls **async**; after every 5 pages (default) it sends:
  ```json
  {
    "https://example.com/about": { ... },
    "https://example.com/contact": { ... }
  }
  ```
- Connection closes automatically when crawl ends or on error.

---

## CLI & Frontend
| Tool | Location | Usage |
|------|----------|-------|
| **Shell Runner** | `run.sh` | Activates venv, starts dev server. |
| **Minimal UI** | `static/index.html` + `static/script.js` | Paste URL ➜ see JSON prettified in the browser. |

---

## Project Structure
```
web_scraper/
│
├── app/                    # FastAPI backend
│   ├── config.py           # Tunables (timeouts, log level)
│   ├── main.py             # App entry-point
│   ├── models/             # Pydantic schemas
│   ├── routes/             # API + WebSocket endpoints
│   └── scraper/            # fetcher, parser, utils
│
├── static/                 # Front-end assets
├── tests/                  # pytest suites
├── requirements.txt
└── run.sh
```

---

## Testing
```bash
pytest -q
```
- **Unit** – HTML parsing, fetcher timeouts.  
- **Integration** – Spin up FastAPI with `TestClient`, hit `/scrape`, expect structured JSON.  

> CI-ready: hook into GitHub Actions → run on every push for free.

---

## Contributing
Got an idea or bug?  
1. **Fork** → create feature branch → commit **atomic**, well-scoped changes.  
2. Run `pre-commit` hooks locally.  
3. Open a pull request; describe *what* & *why*.  
We squash-merge after CI passes.

---

## License
[MIT](LICENSE) – free to use, modify, and ship. Just keep the copyright.

---

> Built by Vasu Bhut – because reliable data scraping shouldn’t be a pain. ✌️