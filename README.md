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
git clone [<repository-url>](https://github.com/Harikrishna1408-nxtwave/sports-quiz-agent.git)

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

Screenshots of the project.

- Home Page <img width="1917" height="1011" alt="Screenshot 2026-07-20 164405" src="https://github.com/user-attachments/assets/0c7e5e37-46a8-4412-98a0-f7a7e9540a75" />
- Quiz Generated <img width="1917" height="1012" alt="Screenshot 2026-07-20 164125" src="https://github.com/user-attachments/assets/3d19b0e0-b313-43d8-a8f9-a8d0ce31eec6" />
- Score Screen <img width="1917" height="1012" alt="Screenshot 2026-07-20 164319" src="https://github.com/user-attachments/assets/ddbdfb3f-fe71-4461-8afe-034ffa65174a" />
- RAG Evidence <img width="1917" height="1007" alt="Screenshot 2026-07-20 164031" src="https://github.com/user-attachments/assets/5a3d74ee-1505-4e64-a131-a383391ce0c9" />

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
