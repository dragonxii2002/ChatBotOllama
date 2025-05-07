from langchain_ollama import ChatOllama

# Initialize the chat model
chat = ChatOllama(model="Mistral")

# Run the chat loop
while True:
    user_input = input("You: ")  # Get user input
    if user_input.lower() in ["exit", "quit", "close"]:  # Check if user wants to exit
        print("Closing the chat. Goodbye!")
        break
    response = chat.invoke(user_input)  # Get AI response
    print("AI:", response)  # Print AI response