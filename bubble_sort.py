"""
    usage: python3 bubble_sort.py --input_list 1,2,4,2,12 --sort_order 2
"""
import argparse


def bubble_sort(input_list, sort_order):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1] if sort_order is 1 else input_list[j] < input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    print(input_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take input list and key to be found')
    parser.add_argument('--input_list', help="List of inputs", type=str)
    parser.add_argument('--sort_order', help="1 for asc, 2 for desc", type=int)
    args = parser.parse_args()

    list_to_be_sorted = [int(list_item) for list_item in args.input_list.split(',')]
    bubble_sort(list_to_be_sorted, args.sort_order)
