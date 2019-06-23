import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from googletrans import Translator
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(
        "Vietnames ChatBot",
        database='db.sqlite3',
        logic_adapters=[
            "chatterbot.logic.BestMatch"
        ]
    )
    # trainer = ChatterBotCorpusTrainer(chatterbot)
    trainer = ListTrainer(chatterbot)
    trainer.train("example_app/training_file.json")
    trainer.train([
            "Hello",
            "Hi you! How I can help you",
            "Hi",
            "Hi you! How I can help you",
            "What your name?",
            "My name is V-AI-Chatbot!",
            "Who are you?",
            "I am an artificial intelligence! You ask me in English, I will answer in Vietnamese",
            "where are you from?",
            "I am from Viettel company! I am made by IT team at medical room",
            "How are you?",
            "I am happy! and you?",
            "I'm also good.",
            "That's good to hear.",
            "Yes it is.",
            "What is your favorite book?",
            "I can't read.",
            "So what's your favorite color?",
            "Blue"
        ])
    trainer = ChatterBotCorpusTrainer(chatterbot)
    trainer.train("chatterbot.corpus.english")
    trainer.train("example_app/training_file.json")

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))
        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)
        translator = Translator()
        response_data = translator.translate(str(response),src='en', dest='vi').text
        response_data = '{"text":"'+response_data+'"}'
        return JsonResponse(json.loads(response_data), status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
