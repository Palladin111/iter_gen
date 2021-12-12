nested_list = [['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None],]

def generator(nested_list):

    for char in nested_list:
        for char_1 in char:
            yield char_1

for item in generator(nested_list):
            print(item)


