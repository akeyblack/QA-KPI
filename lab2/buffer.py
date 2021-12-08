from config import MAX_BUF_FILE_SIZE


class Buffer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Wrong name")
        else:
            self.name = name
            self.queue = []

    def push(self, item):
        if len(self.queue) == MAX_BUF_FILE_SIZE:
            print("Can't add anymore")
        else:
            self.queue.append(item)

    def consume(self):
        if len(self.items) == 0:
            return None
        return self.queue.pop()
