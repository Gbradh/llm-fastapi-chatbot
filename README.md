# 🤖 LLM-Powered Chatbot with FastAPI & SQL Integration

This is a simple yet powerful chatbot application that combines a Large Language Model (LLM) via Groq API with a FastAPI backend, SQLite/PostgreSQL database, and an optional ReactJS frontend.

The chatbot can understand natural language queries and respond with data pulled from a customer database — by automatically generating and executing SQL queries using the LLM.

---

## 📌 Features

- 🔍 Accepts natural language input (e.g., “Show me all female customers from Mumbai”)
- 🧠 Uses Groq-hosted LLM (LLaMA 3.1 / Mistral-7B) to convert input to SQL
- 🗃️ Queries a real SQLite or PostgreSQL database
- ⚡ FastAPI backend for quick and scalable API
- 💻 Optional ReactJS frontend or Postman testing
- 🧾 Logging and error handling included
- 🔐 Environment variable support for API keys

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Backend     | Python, FastAPI   |
| LLM         | Groq API (LLaMA 3.1 or Mistral-7B) |
| Database    | SQLite3 (or PostgreSQL) |
| Frontend    | ReactJS *(optional)* |
| ORM         | SQLAlchemy        |
| Env Config  | python-dotenv     |

---

## ⚙️ Project Structure
llm_chatbot/
├── backend/
│ ├── main.py # FastAPI app
│ ├── models.py # SQLAlchemy models
│ ├── database.py # DB connection setup
│ ├── groq_client.py # (optional) Groq LLM integration
│ ├── seed_data.py # Seeds initial customer data
│ └── .env # Environment variables (not pushed to GitHub)
├── frontend/ # React app (optional)
├── README.md
├── .gitignore


