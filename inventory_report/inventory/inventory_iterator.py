from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            return_data = self.data[self.index]
            self.index += 1
            return return_data
        except IndexError:
            raise StopIteration()
