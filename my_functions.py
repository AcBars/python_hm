import random
def rndint_array(len_array, min_el=-100, max_el=101):
    """The function creates a list consisting of int numbers of a given length.
    By default, the list items are set from -100 to 100.
    You can additionally specify the maximum and minimum values of a list item."""
    arr = []
    for _ in range(0, len_array):
        arr.append(random.randrange(min_el, max_el))
    return arr

def rndfloat_array(len_array, dec_places=3, min_el=-100.000, max_el=101.000):
    """The function creates a list consisting of floating-point numbers of a given length.
        By default, the list items are set in the range from -100 to 100.
        You can additionally specify the maximum and minimum values of the list item and the number of decimal places."""
    arr = []
    for _ in range(0, len_array):
        arr.append(round(random.uniform(min_el, max_el), dec_places))
    return arr
