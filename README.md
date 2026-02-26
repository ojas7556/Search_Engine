# 🔎 LangChain Search Agent Chatbot (Streamlit + Groq)

A Streamlit-based AI chatbot powered by **LangChain** and **Groq LLM** that can answer user queries by intelligently using multiple external knowledge sources such as **web search, Wikipedia, and Arxiv**. The agent performs reasoning, selects appropriate tools, and delivers responses in an interactive chat interface.

---

## 🚀 Features

* 💬 ChatGPT-style Streamlit interface
* 🤖 ReAct AI agent using LangChain
* 🌐 Web search via DuckDuckGo
* 📚 Wikipedia knowledge retrieval
* 🧠 Arxiv research paper lookup
* ⚡ Groq Llama model for fast inference
* 🧾 Persistent chat history using Streamlit session state
* 🔍 Transparent reasoning via Streamlit callback handler

---

## 🧱 Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Groq (Llama 3.1 model)**
* **DuckDuckGo Search**
* **Wikipedia API**
* **Arxiv API**

---

## 📦 Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/your-username/langchain-search-agent.git
cd langchain-search-agent
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a Groq account and obtain an API key.

You can either:

* Enter the key directly in the Streamlit sidebar UI
  **OR**
* Store it in a `.env` file

```
GROQ_API_KEY=your_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters a question in the chat interface
2. LangChain ReAct agent analyzes the query
3. Agent selects an appropriate tool (Search / Wikipedia / Arxiv)
4. Tool returns information
5. Agent synthesizes a final response
6. Conversation is stored and displayed

---

## 📁 Project Structure

```
langchain-search-agent/
│
├── app.py
├── requirements.txt
├── README.md
└── .env (optional)
```

---

## ⚠️ Known Limitations

* Conversation memory is UI-level only (not full agent memory)
* Tool selection depends on LLM reasoning quality
* Requires valid Groq API key

---

## 🔮 Future Improvements

* Add persistent vector memory
* Migrate to LangGraph for production agents
* Multi-agent planner/executor architecture
* Token streaming UI
* Tool analytics dashboard

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

* LangChain community
* Groq inference platform
* Streamlit ecosystem
