nested_list = [['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None],]

class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.new_list = []
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i < len(self.nested_list):
            self.char = self.nested_list[self.i]
            self.new_list.extend(self.char)
            self.i += 1

        if self.j < len(self.new_list):
            self.char_1 = self.new_list[self.j]
            self.j += 1

            return self.char_1

        else:
            raise StopIteration

for item in FlatIterator(nested_list):
    print(item)
