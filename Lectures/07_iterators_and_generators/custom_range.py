class custom_range:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current_start = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_start += 1
        if self.current_start <= self.end:
            return self.current_start
        raise StopIteration


one_to_ten = custom_range(1, 100)
for num in one_to_ten:
    print(num)
