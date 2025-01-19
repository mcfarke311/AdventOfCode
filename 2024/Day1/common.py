import argparse
from sys import argv
from pathlib import Path
import re

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