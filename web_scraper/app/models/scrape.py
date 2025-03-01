from pydantic import BaseModel, HttpUrl

class ScrapeRequest(BaseModel):
    url: HttpUrl

class ScrapeResponse(BaseModel):
    title: str
    headings: list[str]
    paragraphs: list[str]
    links: list[str]