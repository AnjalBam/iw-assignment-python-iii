"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
f) Binary search
"""
sample_lst = [12, 8, 6, 14, 9, 5, 1, 6]

search_item = 14


def binary_search(lst, item):
    """
    :returns the index of the first item found in the list
    """
    n = len(lst)-1
    if item != lst[-1] and n > 1:
        mid = n // 2  # find the mid element
        if lst[mid] == item:
            return mid  # return the index if matches
        elif item > lst[mid]:
            # calls itself with latter half if greater than mid element
            return binary_search(lst[mid:], item)
        else:
            # calls itself with former half if smaller than mid element
            return binary_search(lst[:mid], item)
    return -1  # returns the -1 if not found


print(binary_search(sample_lst, search_item))
