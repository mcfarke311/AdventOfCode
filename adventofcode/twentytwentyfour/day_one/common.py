import argparse
from sys import argv
from pathlib import Path
import re


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