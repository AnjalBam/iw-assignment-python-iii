"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
e) Linear search
"""
sample_lst = [12, 8, 6, 14, 9, 5, 1, 6]

search_item = 14


def linear_search(lst, item):
    for i in range(len(lst)):
        if item == lst[i]:
            return i
    return -1


print(linear_search(sample_lst, search_item))

