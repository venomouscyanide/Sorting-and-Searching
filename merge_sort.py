"""
    Ascending order sorting only. Switch the conditions for descending order sorting.
    usage: python3 merge_sort.py --input_list 102,4,111,24,5555
"""

import argparse


def merge_sort(list_to_be_sorted):
    if len(list_to_be_sorted) > 1:
        mid = len(list_to_be_sorted) // 2
        left_half = list_to_be_sorted[:mid]
        right_half = list_to_be_sorted[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_to_be_sorted[k] = left_half[i]
                i = i + 1
            else:
                list_to_be_sorted[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            list_to_be_sorted[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            list_to_be_sorted[k] = right_half[j]
            j = j + 1
            k = k + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take input list and key to be found')
    parser.add_argument('--input_list', help="List of inputs", type=str)
    args = parser.parse_args()

    list_to_be_sorted = [int(list_item) for list_item in args.input_list.split(',')]
    merge_sort(list_to_be_sorted)
    print(list_to_be_sorted)
