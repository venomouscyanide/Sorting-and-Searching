"""
    usage: python3 selection_sort.py --input_list 1,2,4,2,12 --sort_order 2
"""

import argparse


def selection_sort(list_to_be_sorted, sort_order):
    for i in range(0, len(list_to_be_sorted) - 1):
        for j in range(i + 1, len(list_to_be_sorted)):
            if list_to_be_sorted[i] > list_to_be_sorted[j] if sort_order is 1 else list_to_be_sorted[i] < list_to_be_sorted[j]:
                list_to_be_sorted[i], list_to_be_sorted[j] = list_to_be_sorted[j], list_to_be_sorted[i]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take input list and key to be found')
    parser.add_argument('--input_list', help="List of inputs", type=str)
    parser.add_argument('--sort_order', help="1 for asc, 2 for desc", type=int)
    args = parser.parse_args()

    list_to_be_sorted = [int(list_item) for list_item in args.input_list.split(',')]
    selection_sort(list_to_be_sorted, args.sort_order)
    print(list_to_be_sorted)
