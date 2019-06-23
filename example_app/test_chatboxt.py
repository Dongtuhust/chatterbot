from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)
trainer = ListTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train([
            "Hello",
            "Hi you! How I can help you",
            "Hi",
            "Hi you! How I can help you",
            "What your name?",
            "I am Vietnames ChatBot!  I will answer in Vietnamese",
            "Who are you?",
            "I am VietnamesChatBot! You ask me in English, I will answer in Vietnamese"
        ])

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
while True:
		message = input('You:')
		if message.strip() != 'Bye':
				reply = chatbot.get_response(message)
				print('ChatBot:', reply)
				
		if message.strip() == 'Bye':
				print('ChatBot: Bye')
				break