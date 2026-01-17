def answer_prompt(context: str, question: str) -> str:
    return f"""
You are a helpful AI assistant.

Context:
{context}

User Question:
{question}

Answer clearly and concisely:
"""
