import argparse
import os
import sys
from utils.config import load_config, check_and_create_project_dir
from app import initialize, config
from utils.colorized_cli_utils import console

# TODO: review, maybe consolidate the handlers into one file
from handlers.init_handler import handle_init
from handlers.cli_args import handle_new
from watchers import watch_directory
from rich import print
from config.cli_parser import parser, cmd_parser


def main():
    print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
    # preloading and initializing the app
    initialize()
    # Load the config file

    args = parser.parse_args()

    response = cmd_parser(args)
    print(response)

    if not config:
        print("Exiting...")
        return

    # Now you can access the values with args.new, args.template, args.name, args.path
    # Add your logic here


if __name__ == "__main__":
    main()
