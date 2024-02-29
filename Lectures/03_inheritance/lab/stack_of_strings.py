class Stack:

    def __init__(self):
        self.data: list = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        return "[" + ', '.join(f"{element}" for element in self.data[::-1]) + "]"
