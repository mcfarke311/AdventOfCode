#!/usr/bin/env python3

from adventofcode.twentytwentyfour.common import parse_arguments
from .common import get_input_lists


def calculate_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    """Calculate the similarity score of two lists

    :param left_list: one of the lists to compare
    :type left_list: list[int]
    :param right_list: The other list to compare
    :type right_list: list[int]
    :return: The similarity score of the two lists
    :rtype: int
    """    
    return sum([number * right_list.count(number) for number in left_list])


def main():
    """Main workflow"""
    args = parse_arguments()
    list_one, list_two = get_input_lists(args.input)
    similarity_score = calculate_similarity_score(list_one, list_two)
    print(similarity_score)


if __name__ == "__main__":
    main()
