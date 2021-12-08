from config import DIR_MAX_ELEMS
from binary import Binary
from buffer import Buffer
from log import Log


def is_system_item(item):
    return isinstance(item, (Binary, Log, Buffer, Directory))


class Directory:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Wrong name")
        else:
            self.items = []
            self.name = name

    def delete(self, name):
        if is_system_item(name):
            self.items.remove(name)
        else:
            print("Item isn't a System Item")

    def get_content(self, level=0):
        print(level * "  " + self.name)
        for item in self.items:
            if isinstance(item, Directory):
                item.get_content(level + 1)
            else:
                print((level+1) * "  " + item.name)

    def move(self, item, dest):
        if is_system_item(item):
            if isinstance(item, Directory):
                dest.append(item)
                self.delete(item)
            else:
                print("Destination isn't a Directory")
        else:
            print("Item isn't a System Item")

    def append(self, item):
        if is_system_item(item):
            if len(self.items) == DIR_MAX_ELEMS:
                print("Cant append anymore")
            else:
                self.items.append(item)
        else:
            print("Item isn't a System Item")
        return
