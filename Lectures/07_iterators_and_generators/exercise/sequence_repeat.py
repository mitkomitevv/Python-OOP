class sequence_repeat:

    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.num - 1:
            raise StopIteration

        self.idx += 1
        return self.seq[self.idx % len(self.seq)]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
