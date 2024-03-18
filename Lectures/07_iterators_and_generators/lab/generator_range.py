def genrange(start, stop):
    while start <= stop:
        yield start
        start += 1


print(list(genrange(1, 10)))
