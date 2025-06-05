# 🧠 Streamlit SQL Agent with LangChain & MySQL

An interactive **Streamlit web app** that connects to a **MySQL database**, enabling users to perform natural language queries using **LangChain**, **LLMs via Ollama**, and intelligent SQL generation.

This project is fully containerized using **Docker Compose**, with three services:
- `app`: Python + Streamlit
- `mysql`: MySQL 8.4 database, auto-initialized with the Chinook schema
- `ollama`: Local LLM server for processing natural language queries

---

## 🔧 Features

- Ask questions in natural language → receive SQL-powered answers
- Pre-loaded with the [Chinook database](https://github.com/lerocha/chinook-database)
- Works fully offline using local LLMs (like `llama2`, `mistral`)
- Built with LangChain agents and tools

---

## 🚀 Tech Stack

- [Streamlit](https://streamlit.io/) — interactive frontend
- [MySQL 8.4](https://www.mysql.com/)
- [LangChain](https://www.langchain.com/) — agent, tool, and SQL chaining
- [Ollama](https://ollama.com/) — self-hosted LLM backend (e.g., `mistral`)
- [Docker Compose](https://docs.docker.com/compose/) — local orchestration

---

## 📦 Getting Started (via Docker)

### 1️⃣ Prerequisites

- [Docker](https://docs.docker.com/get-docker/) & Docker Compose installed
- [Ollama](https://ollama.com/download) CLI installed and model pulled:
  
## bash (In your external terminal)
```ollama pull mistral```

## Clone the repo
```git clone https://github.com/Danish8680/sql-agent-streamlit.git```
```cd sql-agent-streamlit```


## Run command
```docker-compose up --build```
