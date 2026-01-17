def search_knowledge_base(query: str) -> str:
    knowledge_base = {
        "mcp": (
            "MCP (Model Context Protocol) is an open protocol that standardizes "
            "how context such as tools, data sources, and prompts are provided "
            "to LLM applications."
        ),
        "anthropic": (
            "Anthropic is an AI research company that developed MCP to enable "
            "rich, modular, and scalable AI applications."
        ),
    }

    return knowledge_base.get(
        query.lower(),
        "No relevant context found in the knowledge base."
    )
