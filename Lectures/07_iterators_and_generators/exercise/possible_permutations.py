from itertools import permutations


def possible_permutations(mylist: list):
    for el in permutations(mylist):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
