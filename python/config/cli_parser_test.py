import pytest
from unittest.mock import MagicMock
from main import main
import argparse
from utils.colorized_cli_utils import print_info
from config.cli_parser import NO_ARGS_FOUND, cli_args, parser, cmd_parser


# ( [command], expected )


def cli_tests_data():
    """test: generate test data for cli arguments"""
    data = [(["foo"], NO_ARGS_FOUND)]
    for cmd in cli_args:
        data.append(([cmd["command"]], cmd["response"]))
    return data


cliArgsTest = cli_tests_data()


# test that the cli args are parsed as expected
@pytest.mark.parametrize("arg, expected", cliArgsTest)
def test_parse_args(arg, expected):
    """test: cli argument parser"""
    print_info("--- test: cli argument parser ---")

    args = parser.parse_args(arg)
    cmd = cmd_parser(args)

    assert cmd == expected
