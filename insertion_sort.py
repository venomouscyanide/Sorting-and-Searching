"""
    usage: python3 insertion_sort.py 1,2,4,2,12 --sort_order 1
"""
import argparse


def insertion_sort(list_to_sort, sort_order):
    for i in range(0, len(list_to_sort)):
        j = i
        while j > 0 and (list_to_sort[j] < list_to_sort[j - 1] if sort_order is 1 else list_to_sort[j] > list_to_sort[j-1]):
            list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]
            j -= 1

    print(list_to_sort)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take input list and key to be found')
    parser.add_argument('--input_list', help="List of inputs", type=str)
    parser.add_argument('--sort_order', help="1 for asc, 2 for desc", type=int)
    args = parser.parse_args()

    list_to_be_sorted = [int(list_item) for list_item in args.input_list.split(',')]
    insertion_sort(list_to_be_sorted, args.sort_order)
