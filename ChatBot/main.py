'''
Made by - Aditya mangal
Purpose - Python mini project
Date  - 18 october 2020
'''
from termcolor import cprint
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')


if __name__ == "__main__":
    cprint("#" * 50, "magenta")
    cprint((f"A Chatot ").center(50), "yellow")
    cprint("#" * 50, "magenta")

    print('You can exit by type exit\n')
    while True:
        query = input(">> ")
        if 'exit' in query:
            exit()
        else:
            print(chatbot.get_response(query))
