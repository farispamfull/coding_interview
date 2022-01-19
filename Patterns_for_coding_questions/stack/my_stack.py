class Stack:
    def __init__(self):
        self.stack_list = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            return None

        self.size -= 1
        return self.stack_list.pop()

    def seek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def push(self, value):
        self.stack_list.append(value)
        self.size += 1

    def size(self):
        return self.size
