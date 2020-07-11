"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
b) Insertion sort
"""
lst = [12, 8, 6, 14, 9, 5, 1, 6]


def sort_by_insertion_method(sample_list, reverse=False):
    len_of_list = len(sample_list)
    for i in range(len_of_list):
        ref_num = sample_list[i]

        j = i - 1
        if reverse:
            while j >= 0 and sample_list[j] < ref_num:
                sample_list[j + 1] = sample_list[j]
                j -= 1
        else:
            while j >= 0 and sample_list[j] > ref_num:
                sample_list[j + 1] = sample_list[j]
                j -= 1

        sample_list[j + 1] = ref_num


sort_by_insertion_method(lst, reverse=True)
print(lst)
