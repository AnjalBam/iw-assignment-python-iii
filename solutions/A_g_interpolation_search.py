"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
g) Interpolation search
"""
sample_lst = [1, 5, 6, 6, 8, 9, 12, 14]

search_item = 6


def search_interpolation(lst, item, start=0, end=0):
    if not end:
        end = len(lst) - 1
    else:
        end = end-1

    while start <= end and lst[end] >= item >= lst[start]:
        if start == end:
            if lst[start] == item:
                return start
            return -1

        # position of the item
        positon = start + int((item - lst[start])
                              * ((end - start) / (lst[end] -lst[start])))

        if lst[positon] == item:
            return positon
        elif lst[positon] < item:
            start = positon + 1
        else:
            start = positon - 1
    return -1


print(search_interpolation(sample_lst, search_item))