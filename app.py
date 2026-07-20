import streamlit as st

from src.database import initialize_database
from src.generator import generate_quiz

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

# ---------------------------------
# Initialize Database
# ---------------------------------
initialize_database()

# ---------------------------------
# Session State
# ---------------------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------------------------
# Header
# ---------------------------------
st.title("🏆 AI-Powered Sports Quiz Generator")

st.markdown("""
Welcome to the **AI-Powered Sports Quiz Generator**!

Generate intelligent sports quizzes using:

- 🤖 Google Gemini AI
- 📚 ChromaDB Knowledge Base
- 🌐 DuckDuckGo Web Search
- 🔍 Retrieval-Augmented Generation (RAG)

Choose your favorite sport and difficulty level to begin!
""")

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:

    st.header("⚙ Quiz Settings")

    sports = [
        "Cricket",
        "Football",
        "Basketball",
        "Tennis",
        "Badminton",
        "Hockey",
        "Kabaddi",
        "Olympics"
    ]

    difficulties = [
        "Easy",
        "Medium",
        "Hard"
    ]

    selected_sport = st.selectbox(
        "🏅 Select Sport",
        sports
    )

    selected_difficulty = st.selectbox(
        "🎯 Difficulty",
        difficulties
    )

    st.divider()

    if st.button("🚀 Generate Quiz", use_container_width=True):

        with st.spinner("Generating AI Quiz..."):

            try:

                st.session_state.quiz = generate_quiz(
                    selected_sport,
                    selected_difficulty
                )

                st.session_state.submitted = False
                st.session_state.score = 0

                # Remove previous answers
                for key in list(st.session_state.keys()):
                    if key.startswith("answer_"):
                        del st.session_state[key]

            except Exception as e:
                st.error("Unable to generate quiz.")
                st.exception(e)

# ---------------------------------
# Quiz Display
# ---------------------------------
if st.session_state.quiz:

    st.success("✅ Quiz Generated Successfully!")

    questions = st.session_state.quiz["questions"]

    for i, q in enumerate(questions):

        st.markdown("---")

        st.subheader(f"Question {i+1}")

        st.write(q["question"])

        st.radio(
            "Choose your answer",
            options=["A", "B", "C", "D"],
            format_func=lambda option, question=q:
                f"{option}. {question['options'][option]}",
            key=f"answer_{i}"
        )

    st.markdown("---")

    # -------------------------
    # Submit Quiz
    # -------------------------
    if not st.session_state.submitted:

        if st.button("✅ Submit Quiz", use_container_width=True):

            score = 0

            for i, q in enumerate(questions):

                selected = st.session_state.get(f"answer_{i}")

                if selected == q["correct"]:
                    score += 1

            st.session_state.score = score
            st.session_state.submitted = True

            st.rerun()

    # -------------------------
    # Results
    # -------------------------
    else:

        st.metric(
            label="🏆 Your Score",
            value=f"{st.session_state.score}/{len(questions)}"
        )

        st.markdown("## 📖 Review Answers")

        for i, q in enumerate(questions):

            st.markdown("---")

            user_answer = st.session_state.get(f"answer_{i}")

            if user_answer == q["correct"]:
                st.success(f"Question {i+1}: Correct ✅")
            else:
                st.error(f"Question {i+1}: Incorrect ❌")

            st.write(f"**Question:** {q['question']}")
            st.write(f"**Your Answer:** {user_answer}")
            st.write(f"**Correct Answer:** {q['correct']}")

            st.info(q["explanation"])

        # -------------------------
        # RAG Evidence
        # -------------------------
        if "retrieved_context" in st.session_state.quiz:

            st.markdown("---")
            st.subheader("📚 Retrieval-Augmented Generation (RAG) Evidence")

            with st.expander("View ChromaDB Context"):

                st.write(
                    st.session_state.quiz["retrieved_context"]
                )

            with st.expander("View Web Search Results"):

                st.write(
                    st.session_state.quiz.get(
                        "web_results",
                        "No web results available."
                    )
                )

        st.markdown("---")

        if st.button("🔄 Generate Another Quiz", use_container_width=True):

            st.session_state.quiz = None
            st.session_state.submitted = False
            st.session_state.score = 0

            for key in list(st.session_state.keys()):
                if key.startswith("answer_"):
                    del st.session_state[key]

            st.rerun()

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit • Google Gemini • ChromaDB • DuckDuckGo Search"
)