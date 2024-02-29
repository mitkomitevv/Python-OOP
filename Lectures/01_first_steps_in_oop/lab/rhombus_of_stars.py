n = int(input())


def rhombus(size):

    def top_part():
        for row in range(1, size):
            print(f"{' ' * (size - row)}{'* ' * row}")

    def bottom_part():
        for row in range(size, 0, -1):
            print(f"{' ' * (size - row)}{'* ' * row}")

    top_part()
    bottom_part()


rhombus(n)
