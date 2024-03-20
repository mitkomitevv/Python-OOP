def vowel_filter(function):
    def wrapper():
        result = function()
        return [l for l in result if l in "ayouei"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
