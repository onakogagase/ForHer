class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you?",
            "how are you": "I'm just a chatbot, but I'm here to help!",
            "bye": "Goodbye! Have a great day.",
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I'm sorry, I didn't understand that."

def main():
    chatbot = SimpleChatbot()
    
    print("Chatbot: Hello! How can I assist you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
