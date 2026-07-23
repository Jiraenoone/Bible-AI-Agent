# 📖 Bible AI Agent

An AI-powered Bible Question Answering system built with **FastAPI**, **Gemini**, **RAG (Retrieval-Augmented Generation)**, **ChromaDB**, and **LINE Official Account**.

This project enables users to ask questions about the Bible through LINE, retrieves relevant Bible verses from the Thai Holy Bible (THSV11), and generates contextual answers using Google's Gemini model.

---

## ✨ Features

* 📖 Ask questions about the Bible in Thai
* 🔍 Semantic search using Vector Database (ChromaDB)
* 🤖 AI-generated answers powered by Gemini
* 📚 Bible verse citation for every response
* 💬 LINE Official Account integration
* 🔄 n8n Workflow Automation
* 🚀 FastAPI REST API
* 📈 Designed with Production-ready architecture

---

## 🏗️ System Architecture

```text
LINE User
     │
     ▼
LINE Messaging API
     │
     ▼
n8n Workflow
     │
     ▼
FastAPI Backend
     │
     ├── XML Parser
     ├── ChromaDB
     ├── Retriever
     ├── Gemini Service
     └── SQLite (Conversation History)
     │
     ▼
Response to LINE
```

---

## 🧠 AI Pipeline

```text
THSV11 XML

↓

XML Parser

↓

Embedding Model

↓

ChromaDB

↓

Semantic Search

↓

Gemini

↓

Answer with Bible References
```

---

## 🛠 Tech Stack

| Category        | Technology                    |
| --------------- | ----------------------------- |
| Backend         | FastAPI                       |
| AI Model        | Gemini 2.5 Flash              |
| Embedding       | intfloat/multilingual-e5-base |
| Vector Database | ChromaDB                      |
| Workflow        | n8n                           |
| Database        | SQLite                        |
| Language        | Python                        |
| API             | LINE Messaging API            |

---

## 📂 Project Structure

```text
Bible-AI-Agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── tsv_verses.xml
│
├── chroma_db/
│
├── scripts/
│   └── build_vector_db.py
│
├── services/
│   ├── parser.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── gemini_service.py
│   └── prompts.py
│
└── tests/
```

---

## 🚀 Roadmap

* [x] Project initialization
* [x] XML Bible parser
* [ ] Create Vector Database
* [ ] Semantic Search
* [ ] Gemini Integration
* [ ] FastAPI API
* [ ] Conversation Memory
* [ ] LINE Official Account
* [ ] n8n Automation
* [ ] Docker Deployment

---

## 📌 Future Improvements

* Multi-language Bible support
* Bible chapter summarization
* Daily Verse notification
* Prayer generation
* Conversation memory
* Admin dashboard
* Docker deployment
* CI/CD Pipeline

---

## ⚠️ Notice

This repository is created for educational and portfolio purposes.

Please ensure that your use of Bible text complies with the applicable license terms of the translation you use.

---

## 👨‍💻 Author

Developed by **Jiraenoone**
