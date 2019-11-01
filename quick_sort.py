"""
    Ascending order sorting only. Switch the conditions for descending order sorting.
    usage: python3 quick_sort.py --input_list 102,4,111,24,5555
"""
import argparse


def quick_sort(list_to_sort):
    quick_sort_helper(list_to_sort, 0, len(list_to_sort) - 1)


def quick_sort_helper(list_to_sort, first, last):
    if first < last:
        split_point = partition(list_to_sort, first, last)

        quick_sort_helper(list_to_sort, first, split_point - 1)
        quick_sort_helper(list_to_sort, split_point + 1, last)


def partition(list_to_sort, first, last):
    pivot_value = list_to_sort[first]

    left_mark = first + 1
    right_mark = last

    sentinel = False
    while not sentinel:

        while left_mark <= right_mark and list_to_sort[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while list_to_sort[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            sentinel = True
        else:
            list_to_sort[left_mark], list_to_sort[right_mark] = list_to_sort[right_mark], list_to_sort[left_mark]

    list_to_sort[first], list_to_sort[right_mark] = list_to_sort[right_mark], list_to_sort[first]

    return right_mark


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take input list and key to be found')
    parser.add_argument('--input_list', help="List of inputs", type=str)
    args = parser.parse_args()

    list_to_be_sorted = [int(list_item) for list_item in args.input_list.split(',')]
    quick_sort(list_to_be_sorted)
    print(list_to_be_sorted)
