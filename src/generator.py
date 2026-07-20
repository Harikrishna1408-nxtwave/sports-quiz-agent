import json

from src.config import client
from src.database import retrieve_context
from src.search import search_web


def generate_quiz(sport: str, difficulty: str):
    """
    Generates a sports quiz using ChromaDB retrieval,
    DuckDuckGo web search, and Google Gemini.
    """

    # Retrieve context from ChromaDB
    chroma_context = retrieve_context(sport)

    # Retrieve latest information from web search
    web_context = search_web(sport)

    # Merge context for the LLM
    combined_context = "\n".join(chroma_context + web_context)

    # Prompt
    prompt = f"""
You are an expert sports quiz generator.

Use the retrieved knowledge below to generate an accurate quiz.

If the retrieved context is insufficient, you may use your general sports knowledge.

Sport: {sport}
Difficulty: {difficulty}

Retrieved Context:
{combined_context}

Generate EXACTLY 5 multiple-choice questions.

Requirements:
- Return ONLY valid JSON.
- Do NOT include markdown.
- Do NOT wrap the response inside ```json.
- Every question must contain:
    - question
    - options (A, B, C, D)
    - correct answer
    - explanation
- Only ONE option should be correct.
- Questions should match the selected difficulty.
- Questions should be unique.

Return JSON in this exact format:

{{
    "questions": [
        {{
            "question": "...",
            "options": {{
                "A": "...",
                "B": "...",
                "C": "...",
                "D": "..."
            }},
            "correct": "A",
            "explanation": "..."
        }}
    ]
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        text = response.text.strip()

        # Remove markdown code fences if present
        if text.startswith("```"):
            lines = text.splitlines()
            lines = [
                line
                for line in lines
                if not line.startswith("```")
            ]
            text = "\n".join(lines).strip()

        quiz = json.loads(text)

        # Attach retrieval information for display
        quiz["retrieved_context"] = chroma_context
        quiz["web_results"] = web_context

        return quiz

    except json.JSONDecodeError:
        raise ValueError(
            f"Gemini returned invalid JSON.\n\n{text}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Failed to generate quiz: {str(e)}"
        )