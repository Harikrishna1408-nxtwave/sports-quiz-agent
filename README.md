# 🏆 AI-Powered Sports Quiz Generator

An AI-powered quiz generator that creates dynamic sports quizzes using Retrieval-Augmented Generation (RAG), Google Gemini AI, ChromaDB, and live web search.

---

## 🚀 Features

- 🏏 Multiple Sports Support
- 🎯 Difficulty Levels (Easy, Medium, Hard)
- 🤖 AI-generated MCQs
- 📚 ChromaDB Knowledge Retrieval
- 🌐 Live Web Search Integration
- 🔍 Retrieval-Augmented Generation (RAG)
- ✅ Quiz Submission & Score Calculation
- 📖 Answer Explanations
- 🔄 Generate New Quiz
- 💻 Interactive Streamlit UI

---

## 🛠️ Tech Stack

- Python 3.11
- Streamlit
- Google Gemini 3.5 Flash
- ChromaDB
- Sentence Transformers
- DuckDuckGo Search
- LangChain (optional)

---

## 📂 Project Structure

```
sports-quiz-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   └── sports_facts.json
│
├── chroma_db/
│
└── src/
    ├── config.py
    ├── database.py
    ├── generator.py
    ├── search.py
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd sports-quiz-agent

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

Add screenshots here after running the project.

- Home Page
- Quiz Generated
- Score Screen
- RAG Evidence

---

## 🔮 Future Enhancements

- Timer-based quiz
- User login
- Leaderboard
- Question history
- More sports
- Export results as PDF

---

## 👨‍💻 Author

Harikrishna Bogudamida

Built using Streamlit, Google Gemini, ChromaDB, and DuckDuckGo Search.
