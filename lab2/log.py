class Log:
    def __init__(self, name, content=''):
        if not isinstance(name, str):
            raise ValueError("Wrong name")
        else:
            self.name = name
            if not isinstance(content, str):
                content = ''
            self.content = content

    def readfile(self):
        return self.content

    def append(self, text):
        if not isinstance(text, str):
            print("Not a string!")
        else:
            self.content += text
