#!/usr/bin/env/python3

import argparse
from sys import argv
from pathlib import Path

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