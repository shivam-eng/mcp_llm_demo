📘 **MCP-Inspired AI Chatbot with Anthropic Claude**

🚀**Overview**

This project demonstrates a production-style implementation inspired by the Model Context Protocol (MCP) to build rich-context AI applications using Anthropic Claude.

Instead of hard-coding data access into the LLM, the system separates:

• Context providers (tools, data, prompts)

• LLM invocation logic

This mirrors how modern AI agents and enterprise GenAI platforms are designed.

🧠 **Key Concepts Demonstrated**

• Model Context Protocol (MCP) inspired architecture

• Client–server separation for AI context injection

• Tool-based grounding of LLM responses

• Prompt template reuse and versioning

• Secure API key management using environment variables


🏗️ **Architecture**
User

  ↓
  
MCP Client (Chatbot)

  ↓
  
MCP Server

  ├── Tools (knowledge retrieval)
  
  ├── Prompt templates
  
  └── Context providers
  
  ↓
  
Anthropic Claude (LLM)


🔹 MCP Client

• Embedded within the chatbot application

• Requests tools and prompts from the MCP Server

• Injects retrieved context into the LLM prompt


🔹 MCP Server

• Exposes tools, data resources, and prompt templates

• Remains independent of the LLM provider

• Enables reuse across multiple AI clients


📁 **Project Structure**

mcp_anthropic_demo/

│

├── app/

│   ├── client/        # MCP Client + LLM integration

│   ├── server/        # MCP Server (tools & prompts)

│   └── config/        # Environment-based configuration

│

├── run.py             # Application entry point

├── requirements.txt   # Dependencies

└── README.md


🔧 **Technologies Used**

• Python 3.12

• Anthropic Claude (Messages API)

• MCP-inspired design principles

• Environment variable–based secret management

▶️ **How to Run**

1️⃣ Set API Key

export ANTHROPIC_API_KEY="your_api_key_here"

(Windows PowerShell)

setx ANTHROPIC_API_KEY "your_api_key_here"


2️⃣ Install Dependencies

pip install -r requirements.txt


3️⃣ Run the Application

python run.py


🧪 **Example Output**


Input


What is MCP


Output


MCP (Model Context Protocol) is an open standard that defines how external
context such as tools, data sources, and prompt templates can be supplied
to LLM-based applications in a modular and scalable way.


🔐 **Security Considerations**


• API keys are never hardcoded

• Secrets are injected via environment variables

• Ready for integration with cloud secret managers (AWS, GCP, Azure)


🎯 **Why This Project Matters**

• Demonstrates real-world GenAI system design

• Shows understanding beyond prompt engineering

• Aligns with modern AI agent and tool-based architectures

• Easily extensible to FastAPI, RAG, or multi-tool systems


🔮 **Future Enhancements**

• Expose MCP Server via FastAPI

• Add vector database (RAG + MCP hybrid)
• Implement tool selection logic

Support multiple MCP clients

Add tracing, logging, and cost monitoring
