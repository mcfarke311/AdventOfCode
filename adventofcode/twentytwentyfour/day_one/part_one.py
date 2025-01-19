#!/usr/bin/env python3

from adventofcode.twentytwentyfour.common import parse_arguments
from .common import get_input_lists

def calculate_total_distance(list_one: list[int], list_two: list[int]) -> int:
    """calculate the sum total of the distance between pairs in the lists.
    
    :param list_one: first list of integers
    :type list_one: list[int]
    :param list_two: second list of integers
    :type list_two: list[int]
    :return: the total distance between the lists
    :rtype: int
    """
    # This is about the longest comprehension that I would want to use
    # any longer and it becomes unreadable
    return sum(
        [abs(pair[1] - pair[0]) for pair in zip(sorted(list_one), sorted(list_two))]
    )


def main():
    """Main workflow"""
    args = parse_arguments()
    list_one, list_two = get_input_lists(args.input)
    total_distance = calculate_total_distance(list_one, list_two)
    print(total_distance)


if __name__ == "__main__":
    main()
