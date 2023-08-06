from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create and set up a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Chat with the bot
print("Bot: Hello! How can I help you today?")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    
    response = chatbot.get_response(user_input)
    print("Bot:", response)
