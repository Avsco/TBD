class User:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
        self.UIs = []

    def addUI(self, UI):
        self.UIs.append(UI)