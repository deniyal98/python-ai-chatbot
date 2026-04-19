def chatbot():
    print("🤖 Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi there! How can I help you?")
        elif user == "how are you":
            print("Chatbot: I'm just a bot, but I'm doing great!")
        elif user == "job":
            print("Chatbot: I can help you prepare for interviews.")
        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()
