from app.server.tools import search_knowledge_base
from app.server.prompts import answer_prompt


class MCPServer:
    """
    Acts as an MCP Server.
    Provides tools, data resources, and prompt templates.
    """

    def get_tool(self, tool_name: str, input_data: str) -> str:
        if tool_name == "search":
            return search_knowledge_base(input_data)

        raise ValueError(f"Tool '{tool_name}' not found")

    def get_prompt(self, context: str, question: str) -> str:
        return answer_prompt(context, question)
