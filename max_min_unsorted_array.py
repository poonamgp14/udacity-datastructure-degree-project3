def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 1:
        return ints
    max_number = ints[0]
    min_number = ints[0]

    for item in ints:
        if item >= max_number:
            max_number = item
        elif item <= min_number:
            min_number = item
    return (min_number, max_number)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((78, 767) == get_min_max([123,689,90,767,78,89])) else "Fail")
# pass
print ("Pass" if ((89, 767) == get_min_max([123,689,90,767,89])) else "Fail")
# pass
print ("Pass" if ([] == get_min_max([])) else "Fail")
# pass
print ("Pass" if ([123] == get_min_max([123])) else "Fail")
# pass
