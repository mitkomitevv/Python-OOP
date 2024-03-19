class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= self.count - 1:
            raise StopIteration

        self.idx += 1
        return self.idx * self.step


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
