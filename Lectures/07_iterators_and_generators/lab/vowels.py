class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o']
        self.index = -1
        self.vowels_in_str = [v for v in self.string if v.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_in_str):
            return self.vowels_in_str[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
