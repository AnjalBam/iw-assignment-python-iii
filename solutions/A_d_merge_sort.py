"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
d) Merge sort
"""
sample_lst = [12, 8, 6, 14, 9, 5, 1, 6]


def sort_list_by_merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2  # Finding the mid of the array
        left_part = lst[:mid]  # getting left half
        right_part = lst[mid:]  # getting right half

        sort_list_by_merge_sort(left_part)  # Sorting the first half
        sort_list_by_merge_sort(right_part)  # Sorting the second half

        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                lst[k] = left_part[i]
                i += 1
            else:
                lst[k] = right_part[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_part):
            lst[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            lst[k] = right_part[j]
            j += 1
            k += 1


sort_list_by_merge_sort(sample_lst)
print(sample_lst)