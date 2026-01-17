from app.client.chatbot_client import ChatbotClient

if __name__ == "__main__":
    bot = ChatbotClient()

    question = "What is MCP"
    answer = bot.ask(question)

    print("\nQuestion:", question)
    print("\nAnswer:")
    print(answer)
