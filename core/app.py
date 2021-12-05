from aiogram.types import Message


class Core:
    def __init__(self, messenger):
        self.messenger = messenger

    def __print_message(self, *args):
        print(f"--- {self.messenger}")
        for val in args:
            if val != None:
                print(val)

    def process(self, username=None, user_id=None, chat_id=None, date=None, text=None):
        self.__print_message(username, user_id, chat_id, date, text)
        return None
