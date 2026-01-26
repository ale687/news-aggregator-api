# 📰 News Aggregator API

A backend project built with **FastAPI** that aggregates news from a public API, processes the data, and exposes clean and consistent endpoints for consumption.

The goal of this project is to practice **backend development, API design, automation, and data processing**, following good architectural practices such as separation of concerns and service layers.

---

## 🚀 Features

- Health check endpoint
- Fetch top news headlines by country and category
- Search news articles by keyword
- Clean and normalized API responses
- Modular architecture (service layer)
- Environment-based configuration
- Interactive API documentation with Swagger

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **Requests**
- **python-dotenv**
- **NewsAPI** (external data source)

---

## 📂 Project Structure

```
app/
├── main.py # FastAPI application and endpoints
├── services/
│ └── news_service.py # Business logic and external API calls
└── init.py
```

---

## 🔧 Setup & Installation

```bash
1️⃣ Clone the repository

    git clone https://github.com/ale687/news-aggregator-api.git
    cd news-aggregator-api

2️⃣ Create and activate a virtual environment

    python -m venv .venv
    source .venv/bin/activate   # Linux / Mac
    .venv\Scripts\activate      # Windows

3️⃣ Install dependencies

    pip install -r requirements.txt

4️⃣ Configure environment variables

    Create a .env file in the project root:

        NEWSAPI_KEY=your_api_key_here

    You can get a free API key from:
    
        👉 https://newsapi.org/

```

## ▶️ Running the Application
```
    uvicorn app.main:app --reload

    The API will be available at:

    API: http://127.0.0.1:8000

    Swagger Docs: http://127.0.0.1:8000/docs

```

---



## 📌 Available Endpoints

#### **Health Check**

```http
  GET /health
```
```json
{
  "status": "ok"
}
```

#### ***Top Headlines***

```http
  GET /news/top
```
* Query parameters:
```
- country (default: us)
- category (optional)
- page_size (default: 10)
```

* Example:
```bash
/news/top?country=us&category=technology
```

#### **Search News**

```http
  GET /news/search
```

* Query parameters:
```
- q (required) – search keyword
- page_size (default: 10)
- sort_by (default: publishedAt)
- language (default: en)
```

* Example:
```bash
/news/search?q=python
```

---

## 🧠 Architecture Notes

- main.py handles HTTP concerns (routing, validation, error handling)
- services/news_service.py contains business logic and external API integration
- Clean separation of responsibilities for better scalability and maintainability

---

## 🎯 Learning Goals

This project focuses on:
- Backend API development
- Clean architecture and modular design
- External API integration
- Data normalization
- Automation and data engineering foundations

---

## 📈 Future Improvements

- Pydantic response models
- Caching layer (in-memory or Redis)
- Database persistence (SQLite/PostgreSQL)
- Authentication & rate limiting
- Dockerization and deployment

---

## 🤝 Feedback

Any feedback, suggestions, or improvements are welcome!

---

## 👤 Author

Claudio Alejandro Ledesma

Backend • Data • Automation Enthusiast

GitHub: https://github.com/ale687

LinkedIn: https://www.linkedin.com/in/claudio-alejandro-ledesma-48b65a365/ 
