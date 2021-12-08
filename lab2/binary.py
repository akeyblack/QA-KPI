class Binary:
    def __init__(self, name, content):
        if not isinstance(name, str):
            raise ValueError("Wrong name")
        else:
            self.name = name
            self.content = content

    def readfile(self):
        return self.content
