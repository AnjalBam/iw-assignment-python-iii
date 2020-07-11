"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
c) Quick sort
"""
sample_lst = [12, 8, 6, 14, 9, 5, 1, 6]


def list_part(lst, lower_l, higher_l):
    """
    This function makes the last element as pivot element and puts it in
    right index in the sorted list and also puts the smaller elements left to it
    and bigger elements right to it
    """
    i = lower_l - 1  # index of lower element
    pivot_el = lst[higher_l]  # pivot element -->  last element
    for j in range(lower_l, higher_l):
        if lst[j] < pivot_el:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]  # swap elements

    lst[i + 1], lst[higher_l] = lst[higher_l], lst[i + 1]
    return i+1


def sort_by_quick_sort(lst, lower_l=0, higher_l=0):
    if not higher_l:
        higher_l = len(lst)-1
    if higher_l > lower_l:
        # get the index after correct positioning of the pivot element
        partition_index = list_part(lst, lower_l, higher_l)

        # sort the elements before the partition index
        sort_by_quick_sort(lst, lower_l, partition_index-1)
        # sort elements after partition index
        sort_by_quick_sort(lst, partition_index+1, higher_l)


sort_by_quick_sort(sample_lst)
print(sample_lst)


