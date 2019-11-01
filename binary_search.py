"""
    usage: python3 binary_search.py --input_list 1,2,3,4,12,44 --search_value 5
"""
import argparse


def binary(search_value, items):
    if len(items) == 0:
        print("Not found")
    else:
        mid = len(items) // 2
        if items[mid] == search_value:
            print("Found !!")
        else:
            if search_value < items[mid]:
                binary(search_value, items[:mid])
            else:
                binary(search_value, items[mid + 1:])


def _sorted_check(list_to_be_searched):
    sorted_list_asc = sorted(list_to_be_searched)

    if not (list_to_be_searched == sorted_list_asc):
        raise ValueError("The input must be sorted!")


def _run_binary_search_helper(parser_args):
    list_to_be_searched = [int(list_item) for list_item in parser_args.input_list.split(',')]
    search_value = parser_args.search_value

    _sorted_check(list_to_be_searched)

    binary(search_value, list_to_be_searched)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take input list and key to be found')
    parser.add_argument('--input_list', help='Sorted in ascending order', type=str)
    parser.add_argument('--search_value', help="Value to be found by search", type=int)
    args = parser.parse_args()

    _run_binary_search_helper(args)
