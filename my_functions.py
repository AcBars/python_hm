import random
def rnd_array(len_array, min_el=-100, max_el=101):
    """The function creates a list consisting of int numbers of a given length.
    By default, the list items are set from -100 to 100.
    You can additionally specify the maximum and minimum values of a list item."""
    arr = []
    for _ in range(0, len_array):
        arr.append(random.randrange(min_el, max_el))
    return arr
