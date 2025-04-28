# -Web-Scraper-API-
A simple Python project that scrapes the latest BBC News headlines and serves them through a FastAPI-powered REST API.
webscraper_api/
├── main.py
├── scraper.py
├── requirements.txt
└── README.md
(Python dependencies)
fastapi
uvicorn
requests
beautifulsoup4

 Web Scraper API

A simple FastAPI project that scrapes the latest BBC News headlines and serves them via an API.

## Endpoints

- `GET /` → Welcome message
- `GET /scrape-now` → Scrape BBC News and return headlines

## Run Locally

1. Clone the repository
2. Install dependencies:
