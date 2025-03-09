# Behavioral Patterns
# Iterator Pattern
# Imagine flipping through a photo album.
# The Iterator pattern gives you a way to access elements of a collection (like photos) one by one without exposing the underlying structure.

class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if not self.has_next():
            raise StopIteration
        item = self._collection[self._index]
        self._index += 1
        return item


collection = [1, "two", 3, "four", 5, "six",7,"eight",9,"ten"]
iterator = Iterator(collection)
while iterator.has_next():
    print(iterator.next())
