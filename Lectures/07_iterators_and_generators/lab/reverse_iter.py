class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.end = len(iterable)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.end -= 1
        if self.end >= self.start:
            return self.iterable[self.end]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
