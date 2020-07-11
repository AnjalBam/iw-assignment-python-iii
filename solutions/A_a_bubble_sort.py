"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
a) Bubble sort
"""
sample_list = [12, 8, 6, 14, 9, 5, 1, 6]


def bubble_sort_list(lst, reverse=False):
    """
    :param lst: Takes the list to sort 
    :param reverse: result is Descending order if True
    :return: does not return anything but just sorts the list
    """
    len_of_list = len(lst)

    for i in range(len_of_list):
        is_swapped = False
        for j in range(len_of_list):
            if reverse:
                if sample_list[i] > sample_list[j]:
                    # swap the values
                    sample_list[i], sample_list[j] = sample_list[j], sample_list[i]
                    is_swapped = True
            else:
                if sample_list[i] < sample_list[j]:
                    # swap the values
                    sample_list[i], sample_list[j] = sample_list[j], sample_list[i]
                    is_swapped = True
        if not is_swapped:
            break


bubble_sort_list(sample_list)
print(sample_list)
