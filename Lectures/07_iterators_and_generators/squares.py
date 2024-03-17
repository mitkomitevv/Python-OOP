def squares(num):
    n = 1
    while n <= num:
        yield n ** 2
        n += 1


print(list(squares(5)))
