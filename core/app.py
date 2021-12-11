class Core:
    def __init__(self, messenger):
        self.messenger = messenger

    def process(self, username=None, user_id=None, chat_id=None, date=None, text=None):
        print(username, user_id, chat_id, date, text)
        return None
