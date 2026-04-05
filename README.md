# Mini GEO Audit API and Structured Data Recommendation Demo

## Project Overview

This project is a lightweight GEO (Generative Engine Optimization) audit prototype built using FastAPI and Python.

The API accepts a public webpage URL, extracts visible page signals such as title, meta description, headings, and image references, then recommends a JSON-LD schema block to improve machine readability for AI search systems.

The goal is to simulate how structured content recommendations can improve AI citation readiness, which aligns with Villion’s product vision of helping pages become more understandable to answer engines and generative search systems.

---

## Architecture Overview

Request Flow:

Client Request
→ FastAPI Endpoint
→ URL Validation using Pydantic
→ HTML Fetch using Requests
→ Parsing using BeautifulSoup
→ Rule-based Schema Recommendation
→ Citation Readiness Score
→ Structured JSON Response

Project Structure:

geo-audit-demo/
│── app/
│   │── main.py
│   │── models.py
│   │── scraper.py
│   │── schema_generator.py
│   │── utils.py
│── requirements.txt
│── README.md

---

## Setup Instructions

1. Create virtual environment:

python -m venv venv

2. Activate environment:

Windows:
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run server:

uvicorn app.main:app --reload

5. Open API docs:

http://127.0.0.1:8000/docs

---

## API Endpoint

POST /audit

Request Example:

{
"url": "https://stripe.com"
}

Response includes:

* title
* meta description
* headings
* image URL
* recommended JSON-LD schema
* citation readiness score

---

## Design Decision Log

### Step 1: Choosing the extraction method

I first considered using Playwright because it can render JavaScript-heavy pages.
However, for an MVP focused on fast implementation and reliability, I chose BeautifulSoup with requests because:

* Faster to implement
* Lower dependency overhead
* Sufficient for many static and semi-static public pages

Trade-off:
This means some client-rendered pages may return incomplete content.

---

### Step 2: Schema recommendation strategy

I considered two approaches:

1. Rule-based schema selection
2. LLM-based semantic classification

I chose rule-based logic for the first version because:

* Output is deterministic
* Easy to explain and debug
* Faster to evaluate during testing

Current schema rules:

* Product keywords → Product schema
* Blog/article keywords → Article schema
* Default homepage/company pages → Organization schema

Trade-off:
This heuristic may misclassify some mixed-content pages.

---

### Step 3: Why no LLM in MVP

An LLM could improve schema accuracy by understanding semantic page intent.

I intentionally did not use an LLM in this version because:

* Extraction itself is deterministic and does not require probabilistic reasoning
* Rule-based output is easier to validate during early-stage prototype work
* Keeping the system dependency-light improves reproducibility

Where an LLM would add value later:

* Detecting business type
* Inferring richer schema properties
* Suggesting missing structured fields

---

### Step 4: Citation Readiness Score

I added a simple citation readiness score to simulate product thinking.

Current scoring:

* title present = 25
* meta description present = 25
* headings present = 25
* image present = 25

This creates a quick visibility signal similar to what a GEO product dashboard might surface.

---

## GEO Relevance to Villion

AI systems rely heavily on structured and machine-readable signals when deciding how confidently to interpret or cite a page.

This prototype improves citation readiness by:

* detecting missing structured signals
* recommending JSON-LD schema
* exposing page meaning in a format AI systems can interpret consistently

A homepage classified as Organization schema, for example, helps answer engines understand entity identity more clearly.

---

## Assumptions

* Public URL is reachable
* Page does not aggressively block HTTP requests
* HTML contains visible metadata
* First detected image is acceptable for MVP output

---

## Known Limitations

* JavaScript-heavy pages may return incomplete extraction
* Relative image URLs are not normalized into absolute URLs
* Schema recommendation uses simple heuristics
* Existing JSON-LD on the page is not yet analyzed

---

## If Scaling to 50+ Pages

For full website auditing, I would redesign into separate components:

Crawler Layer
→ URL Queue
→ Parallel Extraction Workers
→ Schema Recommendation Engine
→ Persistence Layer

Possible additions:

* async crawling
* worker queue (Celery)
* retry handling
* failure logging

Deterministic logic would remain for extraction, while LLMs would be introduced only for semantic schema enrichment.

---

## Biggest Current Weakness

The current implementation does not render browser-executed content.

Improvement with more time:

Add Playwright fallback when extraction confidence is low.

This would improve handling of JavaScript-first websites.

---
