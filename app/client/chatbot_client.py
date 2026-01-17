import anthropic
from app.server.mcp_server import MCPServer
from app.config.settings import (
    ANTHROPIC_API_KEY,
    MODEL_NAME,
    MAX_TOKENS
)


class ChatbotClient:
    """
    Acts as an MCP Client embedded inside an LLM application.
    """

    def __init__(self):
        self.mcp_server = MCPServer()

        if not ANTHROPIC_API_KEY:
            raise EnvironmentError(
                "ANTHROPIC_API_KEY is not set in environment variables"
            )

        self.llm_client = anthropic.Anthropic(
            api_key=ANTHROPIC_API_KEY
        )

    def ask(self, question: str) -> str:
        # Simple keyword extraction for demo purposes
        keyword = question.split()[-1].lower()

        # Fetch context from MCP server (tool call)
        context = self.mcp_server.get_tool("search", keyword)

        # Fetch prompt template from MCP server
        prompt = self.mcp_server.get_prompt(context, question)

        # Call Anthropic LLM
        response = self.llm_client.messages.create(
            model=MODEL_NAME,
            max_tokens=MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.content[0].text.strip()
