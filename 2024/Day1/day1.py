#!/usr/bin/env python3

import argparse
import re
from pathlib import Path
from sys import argv


def parse_arguments(unparsed_arguments: list[str] = argv) -> argparse.Namespace:
    """Parse arguments and get the input file

    :param unparsed_arguments: arguments to be parsed, defaults to argv
    :type unparsed_arguments: list[str], optional
    :return: parsed arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    return args


def get_input_lists(input_file: Path) -> tuple[list[int], list[int]]:
    """get the input lists from a file

    :param input_file: file containing the input lists
    :type input_file: Path
    :return: The lists parsed from the input file
    :rtype: tuple[list[int], list[int]]
    """
    list_one = []
    list_two = []
    with open(input_file, "r") as input_file_text:
        for line in input_file_text.readlines():
            item_one, item_two = re.split(r"\s+", line.strip())
            list_one.append(int(item_one))
            list_two.append(int(item_two))
    return list_one, list_two


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
