from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < self.PHOTOS_PER_PAGE:
                slot = len(self.photos[i]) + 1
                self.photos[i].append(label)

                return f"{label} photo added successfully on page {i + 1} slot {slot}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += f"{('[] ' * len(page)).rstrip()}\n"
            result += "-----------\n"

        return result
